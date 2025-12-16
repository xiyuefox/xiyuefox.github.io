
export default {
  async fetch(request, env) {
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    // Handle GET requests (Serve Image)
    if (request.method === 'GET') {
      const url = new URL(request.url);
      const key = url.pathname.slice(1);
      if (!key) return new Response('Home', { headers: corsHeaders });

      const object = await env.BUCKET.get(key);

      if (object === null) {
        return new Response('Object Not Found', { status: 404, headers: corsHeaders });
      }

      const headers = new Headers();
      object.writeHttpMetadata(headers);
      headers.set('etag', object.httpEtag);
      headers.set('Access-Control-Allow-Origin', '*');

      return new Response(object.body, {
        headers,
      });
    }

    // Handle POST requests (Upload)
    if (request.method === 'POST') {
      try {
        const formData = await request.formData();
        const file = formData.get('file');

        if (!file) {
          return new Response(JSON.stringify({ error: 'No file uploaded' }), {
            status: 400,
            headers: { ...corsHeaders, 'Content-Type': 'application/json' }
          });
        }

        const filename = `${Date.now()}-${file.name}`;

        await env.BUCKET.put(filename, file.stream(), {
          httpMetadata: {
            contentType: file.type,
          },
        });

        const publicUrl = `https://xixi-image-bed.jinxiyue07.workers.dev/${filename}`;

        return new Response(JSON.stringify({
          success: true,
          url: publicUrl
        }), {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });

      } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), {
          status: 500,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });
      }
    }

    return new Response('Method Not Allowed', { status: 405, headers: corsHeaders });
  },
};
