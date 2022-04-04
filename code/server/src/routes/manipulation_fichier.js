
const fs = require("fs");
const path = require("path");

// Permet juste de créer un fichier zip avec tout les fichier data
const child_process = require("child_process")


function dossier_existe(chemin) {
	console.log("chemin:", chemin);
	return new Promise((res, rej) => {
		fs.access(chemin, (err) => {
			console.log("err:", err);
			if (err) res(false);

			res(true);
		});
	});
}

function cree_nom_fichier() {
	/*
	 Crée un nom de fichier au format 'data-MM_DD-hh_mm_ss_msmsms.csv'
	*/
	const date = new Date();

	const jour = `${ date.getMonth() }_${ date.getDay() }`;
	const heure = `${ date.getHours() }_${ date.getMinutes() }_${ date.getSeconds() }_${ date.getMilliseconds() }`;
	
	const nom_fichier = `data-${ jour }-${ heure }.csv`;
	return nom_fichier
}

async function sauvegarde(chemin_data, data) {
	/* 
		Entrées:	- chemin_data doit être un string
							- data doit être un string
		Retourne: null (c'est une procédure)

		Erreurs:	envoie des erreurs si le chemin_data n'est pas accessible
							ou si la création du fichier n'a pas fonctionnée

		Sauvegarde data dans un fichier dans le dossier chemin_data
		le nom de fichier sera format 'data-MM_DD-hh_mm_ss_msmsms.csv'
	*/

	// Si le dossier n'existe pas, on ne peut pas sauvegarder
	const chemin = path.join(__dirname, chemin_data);
	if (!await dossier_existe(chemin)) {
		throw new Error("Le dossier de sauvegarde n'existe pas");
	}

	const nom_fichier = cree_nom_fichier();
	const chemin_sauvegarde = path.join(__dirname, chemin_data, nom_fichier);

	await fs.writeFile(chemin_sauvegarde, data, (err) => {
		if (err) {
			throw err;
		}
	});

	return true;
}


function cree_zip(chemin_sauvegarde) {
	/*
		crée un fichier zip de façon asynchrone
		avec un child process, puis retourne le nom du fichier
	*/
	// Ne fonctionne pas si le chemin de sauvegarde est absolu
	//const chemin_sauvegarde1 = path.join(__dirname, chemin_sauvegarde);

	const chemin = path.join(__dirname, chemin_sauvegarde);

	const nom_fichier_zip = "tmp.zip";
	const chemin_zip = path.join(__dirname, nom_fichier_zip);

	return new Promise((res, rej) => {
		const zip_process = child_process.spawn("tar.exe", ["-caf", chemin_zip, chemin])

		zip_process.on("error", (err) => {
			throw err;
		});

		zip_process.on("exit", (code) => {
			console.log("process exit, code:,", code);
		});

		zip_process.on("stdout", (chunk) => {
			console.log(chunk);
		});

		zip_process.on("close", (code) => {
			res({code, chemin_zip});
		});
	});
}

module.exports = {
	sauvegarde,
	cree_zip
}
