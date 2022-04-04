
const { data_dir } = require("../config.json");
const { cree_zip } = require("./manipulation_fichier");
const fs = require("fs");

module.exports = {
	// Selectionne la requête
	method: "GET",
	route: "/telecharge",

	// 
	handler: async (req, res) => {
		res.writeHead(200);

		const { chemin_zip } = await cree_zip(data_dir);

		const read_stream = fs.createReadStream(chemin_zip);

		read_stream.pipe(res);
		read_stream.on("close", () => {
			res.end();
		});
	}
}

