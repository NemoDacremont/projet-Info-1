
const { data_dir } = require("../config.json");
const { cree_zip } = require("./manipulation_fichier");
const fs = require("fs");

module.exports = {
	// Selectionne la requête
	method: "GET",
	route: "/telecharge",

	// 
	handler: async (req, res) => {
		const { chemin_zip } = await cree_zip(data_dir);

		const read_stream = fs.createReadStream(chemin_zip, { encoding: "binary" });

		res.writeHead(200, {
			"Content-Disposition": "attachment;filename=" + "data.zip",
      'Content-Type': 'application/zip'
		});

		read_stream.pipe(res);
		read_stream.on("close", () => {
			res.end();
		});
	}
}

