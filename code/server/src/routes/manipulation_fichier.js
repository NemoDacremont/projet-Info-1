
const fs = require("fs");
const path = require("path");

// Permet juste de créer un fichier zip avec tout les fichier data
const childa = require("child_process")


function dossier_existe(chemin) {
	return new Promise((res, rej) => {
		fs.access(chemin, (err) => {
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
	if (!await dossier_existe(chemin_data)) {
		throw new error("Le dossier de sauvegarde n'existe pas");
	}

	const nom_fichier = cree_nom_fichier();
	const chemin_sauvegarde = path.join(__dirname, chemin_data, nom_fichier);

	await fs.writeFile(chemin_sauvegarde, data, (err) => {
		console.log(err);
		if (err) {
			throw err;
		}
	});

	return true;
}


async function cree_zip(chemin_sauvegarde) {
	/*
		TODO: crée un fichier zip de façon asynchrone
		avec un child process, puis retourne le nom du fichier
	*/
	const filename = "tmp.zip";
	const chemin = path.join(__dirname, chemin_sauvegarde);


	return filename;
}

module.exports = {
	sauvegarde,
	cree_zip
}
