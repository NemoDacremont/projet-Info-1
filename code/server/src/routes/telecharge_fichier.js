
const manipulation = require("./manipulation_fichier")

module.exports = {
	// Selectionne la requête
	requete: "GET",
	route: "telecharge",

	// 
	handler: (req, res) => {
		req.on("end", () => {
			res.writeHead(200);
			res.end();
		});
	}
}

