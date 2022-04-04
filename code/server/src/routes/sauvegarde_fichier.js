
const { data_dir } = require("../config.json");
const manipulation_fichier = require("./manipulation_fichier");

module.exports = {
	// Selectionne la requête
	method: "POST",
	route: "/sauvegarde",

	// 
	handler: (req, res) => {

		// Stoque les chunk
		const data = []
		req.on("data", (chunk) => {
			data.push(chunk.toString("utf-8"));
		});


		req.on("end", async () => {
			const text = data.join("");
			await manipulation_fichier.sauvegarde(data_dir, text);

			res.writeHead(200);
			res.end();
		});
	}
}
