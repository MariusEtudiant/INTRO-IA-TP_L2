%% Introduction à l'IA - TD 2
%% Un système expert médical en Prolog
%%
%% Etape 1: Charger ce fichier dans SWI-Prolog
%%
%% Guide d utilisation des commandes SWI à utiliser dans votre terminal : https://www.swi-prolog.org/pldoc/man?section=cmdline
%% \!\: vous devez produire un exécutable de ce fichier pour pouvoir l utiliser
%%
%% Etape 2 : Exécuter le fichier en effectuant la requête
%% ?- consultation.
%% (répondre avec ";" à un diagnostic pour avoir le suivant.)
%% ?- effacer.
%% pour effectuer une autre consultation si on n'a pas vu tous les diagnostics.

:- dynamic positif/1.
:- dynamic negatif/1.

consultation :- writeln('Bienvenue au service de consultation expert. Obtenez votre diagnostic !'),
	writeln('Votre nom :'),
	%% Ici, votre nom est sauvegardé dans la variable "Name" qui va etre réutilisé à la fin de la consultation
	readln([Name | _]),
	%% TODO: Le système a besoin des connaissances pour pouvoir fonctionner, à vous de jouer !
	diagnostic(Dis),
	% !, % "ceci si on ne veut qu'un seul diagnostic et ensuite il faut effacer."
	%% Dans ce scénario, le systeme est capable de déterminer la cause
	write(Name), write(', votre diagnostic est : '), writeln(Dis).

%% Dans ce scénario, le systeme n est pas capable de déterminer la cause
consultation :- writeln('Desole, je n\'arrive pas a faire de diagnostic.'),
	effacer.

%% Le prédicat "symptome" prend en argument "X", nous allons donc appeler ce prédicat en donnant une valeur à X qui sera interpreté
symptome(X) :-
	%% On pose une question à l utilisateur en utilisant "X"
	atomic_list_concat(['Avez-vous', X, '? (oui/non)'], ' ', Q),
	%% La variable Q correspond à la réponse que l'on donne à cette question
	sym_positif(Q, X).

sym_positif(_, X) :- positif(X), !.
sym_positif(Q, X) :- not(negatif(X)),
	interroger(Q, X, R), R = [oui].

interroger(Q, X, R) :- writeln(Q), readln(R), enregistrer(X, R).

enregistrer(X, [oui]) :- asserta(positif(X)).
enregistrer(X, [non]) :- asserta(negatif(X)).

% On fait le ménage:
% la commande "retractall" permet d'effacer tous les renseignements (liste de "oui" et/ou de "non") que nous avons donné au système
effacer :-
	retractall(positif(_)),
	retractall(negatif(_)).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% écrire ici la connaissance "experte" permettant de faire des diagnostics
%% sous forme de règles comme celle de cet exemple:

diagnostic(rhume) :-
	symptome('le nez qui coule'),
	symptome('mal a la gorge'),
	symptome('de la conjonctivite').

diagnostic(grippe) :-
	symptome('de la fi�vre'),
	symptome('des maux de t�te'),
	symptome('des douleurs musculaires'),
	symptome('des maux de t�te').


diagnostic(sinusite) :-
	symptome('le nez qui coule'),
	symptome('des maux de t�te'),
	symptome('de la fi�vre'),
	symptome('de la conjonctivite').

diagnostic(meningite) :-
	symptome('des maux de t�te'),
	symptome('de la photophobie'),
	symptome('la nuque raide'),
	symptome('des douleurs musculaires').

diagnostic(angine) :-
	symptome('de la fi�vre'),
	symptome('de la toux'),
	symptome('de la fatigue').

diagnostic(covid) :-
	symptome('de la fi�vre'),
	symptome('de la toux'),
	symptome('de la fatigue'),
	symptome('la perte de l\'odorat').


diagnostic(rhinopharyngite) :-
	symptome('le nez qui coule'),
	symptome('de la toux'),
	symptome('de la fi�vre'),
	symptome('de la fatigue'),
	symptome('des picotements dans le nez').


diagnostic(intoxication_alimentaire) :-
	symptome('de la fi�vre'),
	symptome('des maux de t�te'),
	symptome('des vomissements'),
	symptome('la diarrh�e'),
	symptome('des naus�es').

diagnostic(glaucome) :-
	symptome('tr�s mal � l\'oeil'),
	symptome('une nette baisse de vision'),
	symptome('l\'oeil rouge').
