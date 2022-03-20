# pi-strange
A Raspberry Pi program to control Christmas lights 

For a long time I was annoyed by the primitive and annoying flickering of typical Cristmas lights. It’s easy to make beautiful and interesting, but nobody cares; this makes me to believe that most people don't really have artistic taste in illumination and lighting, so no one cares. But I care and I want my children to have a taste. Looking back from 2022, I can confirm that our hard work paid off: my eldest daughter definitely has taste. 

First problem is that most lights *blink*, which is annoying (and actually considered harmful, especially to people who had some forms of epilepsy). So I decided my lights won't blink, they only will fade.

Second problem is that typical cyclic fading is dull and boring. To make it unpredictable and interesting, I employed the [Lorenz strange attractor](https://en.wikipedia.org/wiki/Lorenz_system). The light intensity follows one of the variables of the system.

The program is supposed to run on the Raspberry Pi computer, however I believe it is easy to adapt for MicroPython environment. It currently controls two channels, but it is easy to add more.
