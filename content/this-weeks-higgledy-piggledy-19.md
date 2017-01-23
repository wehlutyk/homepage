Title: This Week's Higgledy-piggledy
Date: 2017-01-23
Status: published
Category: Higgledy-piggledy
Tags: afrofeminism, history, rust, wikidata
Slug: this-weeks-higgledy-piggledy
Summary: Random assortment of thoughts and links from the last few weeks. Links on Afrofeminism, World history, Rust, and Wikidata.


Links, bits, bobs
-----------------

* [An amazing playlist around Amandine Gay's film «Ouvrir la voix»](https://www.youtube.com/watch?v=NaHIb_Pf_CU&index=1&list=PLbQnIFhNsyY1sOJ1NfpJ3xluuBsfRg3SR) -- excerpts from and debates around a film where black women talk about racism, (post) colonialism, afro-feminism, and their lives, in France and elsewhere. Led me to discover a bit of the afro-feminist blogoshere, including [Many Chroniques](https://manychroniques.blogspot.fr/), [équimauves](https://equimauves.wordpress.com/), [Mrs Roots](https://mrsroots.fr/), [Au bout des lèvres](https://auboutdeslevres.wordpress.com/), [badassafrofem](https://badassafrofem.wordpress.com/), [FANM](https://perleantilles.wordpress.com/). Also fell upon the [Roots](http://www.imdb.com/title/tt0075572/) 1977 mini-series, which seems pretty important given that some of the women in «Ouvrir la voix» discovered the horror of slavery thanks to it (the French school not having done its job properly), and an interesting [Annuaire pour sortir de la recherche blanche et validiste](https://www.fichier-pdf.fr/2015/03/04/annuaire-sortir-de-la-recherche-blanche-et-validiste/annuaire-sortir-de-la-recherche-blanche-et-validiste.pdf). Looking for a political fight reaching for the roots of many of today's questions and problems? This one seems pretty close to exactly that if you ask me.
* [L'histoire de France made in monde](https://www.youtube.com/watch?v=UAaLvhSgENo) -- Peut-on concrètement faire pièce aux publicistes et intellectuels médiatiques qui racontent *ad nauseam* une histoire de France autocentrée servant de combustible au rétrécissement du débat sur «l'identité» ? C'est le pari politique et scientifique d'une *Histoire mondiale de la France*, publiée jeudi 12 janvier. Entretien avec les historiens Patrick Boucheron et Yann Potin.
* [Hamon, Elkrief, les cafés et la pollution](https://www.arretsurimages.net/chroniques/2017-01-23/Hamon-Elkrief-les-cafes-et-la-pollution-id9485) -- aujourd'hui, bonne nouvelle électorale :-)

* [Julia Evans](https://jvns.ca/)' [talk](https://www.youtube.com/watch?v=ftQfpAeyxPo) at RustConf 2016 about how Rust and its community empower you to do things you thought you couldn't do! Her blog (super interesting!) led among other places to [a book on the Linux Virtual Memory manager](https://www.kernel.org/doc/gorman/html/understand/index.html). Cool stuff one discovers is possible to understand!
* And [Josh Triplett](https://twitter.com/josh_triplett)'s [talk](https://www.youtube.com/watch?v=U8Gl3RTXf88) about the Rust RFC process

* Wikidata's [Query Service](https://www.mediawiki.org/wiki/Wikidata_query_service) is absolutely awesome! Let me explain. I started watching Gilmore Girls last week, and was surprised to imagine a small town such as Stars Hollow with such a vibrant community life. Many factors are likely to explain that of course, but one of them might be size. Stars Hollow has a population of about 10,000, so how do I find cities in France and the rest of the world with a population about the same size? [Bam, Wikidata](https://query.wikidata.org/#%23Cities%20with%20population%2010000%2C%20give%20or%20take%201000%0A%0A%23defaultView%3AMap%0ASELECT%20DISTINCT%20%3Fcity%20%3FcityLabel%20%3Fpopulation%20%3Fcoor%20WHERE%20%7B%0A%20%20%3Fcity%20wdt%3AP1082%20%3Fpopulation%20%3B%0A%20%20%20%20%20%20%20%20wdt%3AP625%20%3Fcoor%20.%0A%20%20FILTER%20%28abs%2810000%20-%20%3Fpopulation%29%20%3C%201000%29%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22fr%22%20%7D%0A%7D) (click the blue `Run` button to see the results). Amazing. And so on that map is Orthez, which I know a little, and does indeed give me a feeling similar to Stars Hollow's.


Random thoughts
---------------

None this week.
