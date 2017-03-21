Title: Research
Status: published


At the core, I'm interested in how human beings and other animals *develop*, *grow*, *intermingle* and *communicate*.

This page first explains the overarching [questions](#questions) that drive me and the [sources](#sources) from which I draw inspiration. For more tangible output, jump straight to the [projects](#projects) I've developed, the [publications](#publications) these led to, or my [education](#education).

---

## Questions {id="questions"}

I would like to understand what makes you *you*, what makes me *me*, and what happens in and between us two when we spend time together, when we talk, walk, interact with one another. What happens in a group of more than two people. How what we just exchanged weaves itself in our future interactions. While the end target of this are small groups or dyads, any explanation will most likely include elements of larger groups and dynamics, since all communication takes place in communities where their patterns emerge.

This interest brings me to questions like:

* What exactly is communication, or *meaningful exchange*? What are its minimal forms, and how is everyday language built on top of those minimal forms?
* Communication evolved through time, and continues to do so -- how so? What dynamics and materials bring about communication, under what community conditions?
* How deep is the connection between meaningful exchange and life itself? How do our exchanges and interactions define us? What kind of performance (as in artistic and skilful performance) is meaningful exchange?
* What would a machine need to *be* in order to engage in meaningful exchange? What kind of life evolution can we simulate to bring about in-silico meaningful exchange? (In particular, how much control must we relinquish?) What would be possible with such a creation, and how would it change and mediate our own communication?
* Given the pace of technological change, what better experiments, tools, and methods, can we set up to explore these questions?

(Yes, there's circularity in wanting to understand the process of understanding, but progress on these questions can still be made!)

---

## Epistemic sources {id="sources"}

Some of these contradict each other, but I find them all inspiring:

* The sensorimotor and enactive traditions in Cognitive Science: Alva Noë and Kevin O'Regan, Ezequiel Di Paolo and Hanne De Jaegher, Evan Thompson, Humberto Maturana, Francisco Varela, Daniel Hutto, James Gibson
* The cultural evolution tradition: Dan Sperber, Simon Kirby, and the communities they federate
* Contemporary and previous social anthropology: Mauss's "Les Techniques du Corps", Tim Ingold, Howard Becker, Gregory Bateson, Erving Goffman
* Complex Systems Science: Simon DeDeo, David Krakauer
* Lev Vygotsky and Ludwig Wittgenstein
* David Foster Wallace's reflections on language
* The power of mathematics to structure some questions. The power of some questions to identify mathematics I don't yet know (or that are yet to be invented).

---

## Projects {id="projects"}

### 2015 to now -- [Gistr](https://osf.io/k7d38/)

To investigate interpretation in particular contexts, and the effects it can have at the global scale such as cultural attractors, we built an online *chinese whispers* game where people iteratively memorise and rewrite short pieces of text, to see how they are gradually transformed as they are transmitted.

It's presented as a Game With a Purpose, available a [gistr.io](https://gistr.io). If you're interested, head over to the [project wiki](https://osf.io/k7d38/wiki/)! This was my first non-trivial project using [Elm](http://elm-lang.org/), and it's been a delightful experience.

We're still developing this project and analysing the data it's producing, so more will come here shortly.

<div class="screenshots">
  <a href="/static/gistr-exp-2-screenshots/welcome.png"><img alt="Gistr Welcome page" src="/static/gistr-exp-2-screenshots/welcome.png"></a>
  <a href="/static/gistr-exp-2-screenshots/instructions.png"><img alt="Gistr Experiment Instructions" src="/static/gistr-exp-2-screenshots/instructions.png"></a>
  <a href="/static/gistr-exp-2-screenshots/explore.png"><img alt="Gistr Tree Exploration" src="/static/gistr-exp-2-screenshots/explore.png"></a>
</div>


### 2013-2016 -- [Brains copy-paste](https://brainscopypaste.readthedocs.io/en/latest/)

Online news is full of quotes from politicians or other famous people. Quite often though, those quotes are transformed just a tiny little bit when they are copied from one source to another article -- blog or news outlet. This process is most likely unconscious, but it's not random: the changes made are significant, and we measured some of them with data-mining techniques. Looking at substitutions from one word to another shows that more complex words tend to be replaced with simpler, better known words.

This led to our [*Semantic drift of quotations in blogspace*](https://hal.archives-ouvertes.fr/hal-01143986) paper. The whole analysis is free software and thoroughly documented, so that it can be remixed or can serve as inspiration or as an example for other projects. The code lives [here](https://github.com/wehlutyk/brainscopypaste), the documentation [here](https://brainscopypaste.readthedocs.org/en/latest/).

<div class="screenshots">
  <a href="/static/brainscopypaste-screenshots/figure-4.png"><img alt="Substitution detection models" src="/static/brainscopypaste-screenshots/figure-4.png"></a>
</div>
<div class="screenshots">
  <a href="/static/brainscopypaste-screenshots/figure-6.png"><img alt="Feature susceptibilities" src="/static/brainscopypaste-screenshots/figure-6.png"></a>
  <a href="/static/brainscopypaste-screenshots/figure-5.png"><img alt="POS susceptibilities" src="/static/brainscopypaste-screenshots/figure-5.png"></a>
</div>


### 2012-2014 -- [Daydreaming](https://github.com/daydreaming-experiment)

Mind-wandering is something we all do about 50% of our waking time: at any moment of the day, while reading a book, or working, or during any activity, you can disconnect from the immediate environment and start thinking about the past, the future, or people and places far away. Most of the time you won't even realise it until a few moments have passed, or even not at all! Getting to know more about this phenomenon has been traditionally quite challenging: unconscious mind-wandering isn't something you can trigger on command in the laboratory.

[Vincent Adam](https://vincentadam87.github.io/) and I had partnered to start building Android apps for cognitive science, and after a chance encounter with [Jonathan Smallwood](https://themindwanders.com/) we started a project to gather better data on mind-wandering thanks to smartphones! The project later transitioned to [Mikaël Bastian](http://mikaelbastian.weebly.com/) and [Jérôme Sackur](http://www.lscp.net/persons/sackur/) for the scientific side, partnering with [Gislain Delaire](https://cargocollective.com/gislaindelaire) for the design. Eventually created the [Daydreaming](https://play.google.com/store/apps/details?id=com.brainydroid.daydreaming) app, which would ask you at random moments of the day if you were mind-wandering or not (and delve into the details if you were). Launching it was a nice adventure, and led to another paper, [*Language facilitates introspection*](https://labs.psych.ucsb.edu/schooler/jonathan/sites/labs.psych.ucsb.edu.schooler.jonathan/files/pubs/bastian_innerspeech_manuscript_-_revised_cl-2.pdf), which investigates the effect of mind-wandering in language vs. in images on the probability that you'll realise that you are currently mind-wandering.

<div class="screenshots">
  <a href="/static/daydreaming-screenshots/question.png"><img alt="Daydreaming question example" src="/static/daydreaming-screenshots/question.jpg" style="height: 250px"></a>
  <a href="/static/daydreaming-screenshots/results-rhythms.png"><img alt="Daydreaming rhythms results example" src="/static/daydreaming-screenshots/results-rhythms.png" style="height: 250px"></a>
  <a href="/static/daydreaming-screenshots/results-type.png"><img alt="Daydreaming thought type results example" src="/static/daydreaming-screenshots/results-type.png" style="height: 250px"></a>
</div>

Here too, the whole process was open and all the parts are released as free software: the code is [here](https://github.com/daydreaming-experiment). The project also featured as a pilot experiment for the [Science en Poche](https://iscpif.fr/projects/science-en-poche/) project Vincent and I helped bootstrap with [David Chavalarias](http://chavalarias.com/), securing an "Émergence(s)" grant from the City of Paris later on.


### 2009-2011 -- Rugby

Studying the social and cognitive sides of life together is hard, and a substantial reason for that is that our metaphors and categories might have to change a lot before we can reach satisfying descriptions of cognition-with-social: notably, the separation between the two might not be so obvious. Now another factor is that historically few people have been interested in this topic. So there is much to do, and exhibiting a few strong experimental links between the social and the cognitive is a good place to start to attract interest and spark more debate.

A few years back, with [Julien Clément](https://quaibranly.academia.edu/JulienCl%C3%A9ment) and [Florence Weber](https://fr.wikipedia.org/wiki/Florence_Weber), we started a project aiming to do just that: experimentally show a strong link between the culture we are brought up in and the low-level automatic perception we have of a situation. Such links are probably present everywhere, and the literature in social science is rife with starting points (take Bourdieu's [habitus](https://en.wikipedia.org/wiki/Pierre_Bourdieu#Habitus) for instance), but eliciting one robustly requires a situation where the link is particularly strong and well-identified.

So based on Julien Clément's PhD dissertation (*Le rugby de Samoa: les techniques du corps entre "Fa'Asamoa" et mondialisation du sport*), we aimed to study the way rugby players can perceive a situation differently depending on their upbringing. Samoan players, for instance, contrast strongly with French players: their individual technical competence can be quite superior to that of French players, while being unable to play some team situations that the French would consider textbook, for instance when particular group perception is necessary to win. Julien's work suggests that this strongly relates to players having different low-level perceptions of a given situation, depending on the rugby they have been trained to play, and the social *milieu* they were brought up in.

The goal for the project was to study this hypothesis with the tools of neuroscience, but we had to abort shortly after the preliminary phase because of timing constraints and the lack of clear funding possibilities (among others, funding for a PhD on the subject). The sole output of the endeavour was my [*Rugby et Cognition: Enquête auprès du Racing Métro 92*](/static/2011-rapport-projet-rugby.pdf) internship report studying the Parisian rugby club *Racing Metro 92*, as a first step to identify potential situations where we could develop this idea (since flying international rugby players across the globe for an EEG or MRI is in no lab's budget). Certainly an unrealised opportunity, which might come back to life if the future allows!


---

## Publications {id="publications"}

### Peer-reviewed journals

**Under review**

Sébastien Lerique. [Pour une étude du contexte d’interprétation](https://github.com/wehlutyk/2016-02-article-je-memes/blob/master/article/article.pdf). *Travaux de linguistique*, special issue on "Les mèmes langagiers : Propagation, figement et déformation".


**Published**

Sébastien Lerique and Camille Roth (2017). [The semantic drift of quotations in blogspace: a case study in short-term cultural evolution](https://hal.archives-ouvertes.fr/hal-01143986). *Cognitive Science* (in press).

Mikaël Bastian, Sébastien Lerique, Vincent Adam, Michael S. Franklin, Jonathan W. Schooler, and Jérôme Sackur (2017). [Language facilitates introspection: verbal mind-wandering has privileged access to consciousness](https://labs.psych.ucsb.edu/schooler/jonathan/sites/labs.psych.ucsb.edu.schooler.jonathan/files/pubs/bastian_innerspeech_manuscript_-_revised_cl-2.pdf). *Consciousness and Cognition* (in press).


### Communications

Sébastien Lerique and Camille Roth (2016). Cultural attractors by iterated sentence reformulation: elements of the cognitive story in complex contagion. [*Data Driven Approach to Networks and Language*](https://project.inria.fr/netspringlyon/3-workshops-on-network-sciences/workshop-on-data-driven-approach-to-networks-and-linguistic/), ENS Lyon, May 2016.

Sébastien Lerique (2015). [Pour une étude du contexte d’interprétation](http://slides.com/seblerique/pour-une-etude-du-contexte-d-interpretation). [*Les Mèmes Langagiers* workshop](http://www.stih.paris-sorbonne.fr/?p=1055), Université Paris-Sorbonne, December 2015.

Sébastien Lerique and Camille Roth (2015). [Empirical Attractors in Sentence Reformulation Processes](http://slides.com/seblerique/ccs15-empirical-attractors-in-sentence-reformulation-processes). [*Conference on Complex Systems 2015*](http://www.ccs2015.org/), Arizona State University, September 2015.

Sébastien Lerique (2014). [Cultural Epidemiology. A quest for ontologies where the social and cognitive sciences can meet](https://hal.archives-ouvertes.fr/hal-01144051). *Journée scientifique des doctorants de 1è année de l'ED3C*, Paris, March 2014.

Vincent Adam, Sébastien Lerique, and David Chavalarias (2014). [Pocket Science. Easing development of political, scientific, and citizen apps](https://daydreaming-experiment.github.io/presentation-ccs2014). [*3rd Citizen Cyberscience Summit*](http://cybersciencesummit.org/), University College London, February 2014.

Vincent Adam, Sébastien Lerique, Florence Ruby, Haakon Engen, Gislain Delaire, Tal Yarkoni, and Jonathan Smallwood (2013). [Daydreaming: Exploring mind-wandering with smartphones](https://daydreaming-experiment.github.io/presentation-brainhack2013). [*Brainhack 2013*](http://brainhack.org/brainhack-2013/), Paris, October 2013.


### Project reports

Sébastien Lerique (2016). [The Gistr Platform](https://hal.archives-ouvertes.fr/hal-01361964). Deliverable for the Algopol project ANR-12-CORD-0018.


### Academic theses

Sébastien Lerique (2012). [Comment les cerveaux copient-collent-ils ? Dérive sémantique des citations dans la blogosphère](/static/2012-rapport-stage-m2-cogmaster.pdf). Thesis for the M.Sc. in Cognitive Science *Cogmaster*, directed by Camille Roth. École Normale Supérieure de Paris.

Sébastien Lerique (2011). [Rugby et Cognition. Enquête auprès du Racing Métro 92](/static/2011-rapport-projet-rugby.pdf). Research internship report, directed by Florence Weber and Julien Clément. École Normale Supérieure de Paris.

---

## Education {id="education"}
