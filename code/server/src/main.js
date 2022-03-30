
const http = require("http");

const app = http.createServer();

app.on("request", (req, res) => {
	res.writeHead(400);

	// Sert à stocker les chunks
	const data = []
	req.on("data", (chunk) => {
		data.push(chunk.toString("utf-8"));
	});


	req.on("end", () => {
		const text = data.join("");
		console.log(text);
		res.end();
	})
});

app.listen(8080);
