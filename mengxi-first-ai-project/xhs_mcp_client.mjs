import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { SSEClientTransport } from "@modelcontextprotocol/sdk/client/sse.js";

async function main() {
    console.log("Connecting to XHS MCP...");
    const url = new URL("http://localhost:18060/mcp");
    // Some implementations use `/mcp` as the SSE endpoint
    const transport = new SSEClientTransport(url);
    const client = new Client(
        {
            name: "Antigravity-XHS-Client",
            version: "1.0.0"
        },
        {
            capabilities: {}
        }
    );

    await client.connect(transport);
    console.log("Connected!");
    
    // Check tools 
    const tools = await client.listTools();
    const toolNames = tools.tools.map((t) => t.name);
    console.log("Available tools:", toolNames);

    if (toolNames.includes("search_feeds")) {
        console.log("\nSearching for feeds: 孕35周 营养 运动");
        const res = await client.callTool({
            name: "search_feeds",
            arguments: { keyword: "孕35周 营养 运动" }
        });
        if (res.content && res.content.length > 0) {
            console.log(res.content[0].text.substring(0, 1500));
        } else {
            console.log(JSON.stringify(res, null, 2));
        }
    } else {
        console.log("Tool 'search_feeds' not found.");
    }
    
    process.exit(0);
}

main().catch(err => {
    console.error("Error:", err);
    process.exit(1);
});
