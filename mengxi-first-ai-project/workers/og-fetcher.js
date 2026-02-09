/**
 * OG Archeologist - Cloudflare Worker
 * Fetches OpenGraph metadata from any URL.
 */

addEventListener('fetch', event => {
    event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
    const { searchParams } = new URL(request.url)
    const targetUrl = searchParams.get('url')

    if (!targetUrl) {
        return new Response(JSON.stringify({ error: "No URL provided" }), {
            status: 400,
            headers: { "Content-Type": "application/json" }
        })
    }

    try {
        const response = await fetch(targetUrl, {
            headers: { "User-Agent": "Mozilla/5.0 (compatible; OGFetcher/1.0;)" }
        })
        const html = await response.text()

        const getMeta = (tag) => {
            const match = html.match(new RegExp(`<meta[^>]+(?:property|name)=["'](?:og:|twitter:)?${tag}["'][^>]+content=["']([^"']+)["']`, 'i')) ||
                html.match(new RegExp(`<meta[^>]+content=["']([^"']+)["'][^>]+(?:property|name)=["'](?:og:|twitter:)?${tag}["']`, 'i'))
            return match ? match[1] : null
        }

        const title = getMeta('title') || html.match(/<title>([^<]+)<\/title>/i)?.[1]
        const description = getMeta('description')
        const image = getMeta('image')
        const domain = new URL(targetUrl).hostname

        return new Response(JSON.stringify({
            url: targetUrl,
            title: title?.trim(),
            description: description?.trim(),
            ogImage: image,
            domain: domain
        }), {
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*" // Allow fetch from mengxi.space
            }
        })

    } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), { status: 500 })
    }
}
