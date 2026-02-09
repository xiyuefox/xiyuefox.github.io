addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const url = new URL(request.url)
  let path = url.pathname

  // Default to index.html for root path
  if (path === '/') {
    path = '/index.html'
  }

  // Try to serve the requested file
  try {
    const response = await fetch(`file://${path}`, {
      headers: {
        'Content-Type': getContentType(path),
      },
    })

    if (response.ok) {
      return response
    }
  } catch (error) {
    // If file not found, return 404
    return new Response('404 - File Not Found', { status: 404 })
  }
}

// Determine content type based on file extension
function getContentType(path) {
  if (path.endsWith('.html')) {
    return 'text/html; charset=utf-8'
  } else if (path.endsWith('.css')) {
    return 'text/css'
  } else if (path.endsWith('.js')) {
    return 'text/javascript'
  } else if (path.endsWith('.json')) {
    return 'application/json'
  } else {
    return 'application/octet-stream'
  }
}
