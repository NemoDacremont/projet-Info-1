
const http = require("http");
const routers = require("./routes");

const path = require("path");
const { PORT, data_dir } = require("./config.json");

const app = http.createServer();

app.on("request", (req, res) => {
	console.log(req.method, req.url);

	for (let i=0 ; i<routers.length ; i++) {
		const router = routers[i];

		if (req.method == router.method && req.url == router.route) {
			router.handler(req, res);
			return;
		}
	}

	res.writeHead(400);
	res.end();
});

app.listen(PORT, () => {
	console.log("server listening on port", PORT);
});
