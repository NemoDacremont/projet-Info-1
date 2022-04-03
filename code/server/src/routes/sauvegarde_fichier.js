
const { sauvegarde_fichier } = require("./manipulation_fichier");



module.exports = {
	// Selectionne la requête
	requete: "POST",
	route: "sauvegarde",

	// 
	handler: (req, res) => {

		// Stoque les chunk
		const data = []
		req.on("data", (chunk) => {
			data.push(chunk.toString("utf-8"));
		});


		req.on("end", () => {
			const text = data.join("");
			await sauvegarde_fichier(text);

			res.writeHead(200);
			res.end();
		});
	}
}
