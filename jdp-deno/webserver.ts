const server = Deno.listen({ port: 80 });

for await (const conn of server) {

  console.log(`Servicing a connection at ${new Date()}`);

  serviceConnection(conn);
}

async function serviceConnection(conn: Deno.Conn) {

  const httpConn = Deno.serveHttp(conn);

  for await (const requestEvent of httpConn) {

    const requestBody = requestEvent.request.headers.get("user-agent") ?? "Unknown"
   
    requestEvent.respondWith(
      new Response(requestBody, {
        status: 200,
      }),
    );
  }
}