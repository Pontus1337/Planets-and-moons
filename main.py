
from resources import Planet, Moon



def main():
    tellus = Planet("Tellus",510100000)
    mars = Planet("Mars",144800000)
    jupiter = Planet("Jupiter",61469000000)
    luna= Moon("Luna",37930000)
    phobos=Moon("Phobos",1548)
    deimos=Moon("Deimos",495)
    io=Moon("IO",41910000)
    ganymede=Moon("Ganymede", 87200000)

    luna.add_orbit(tellus)
    deimos.add_orbit(mars)
    phobos.add_orbit(mars)
    io.add_orbit(jupiter)
    ganymede.add_orbit(jupiter)

    tellus.add_moons(luna)
    mars.add_moons(phobos)
    mars.add_moons(deimos)
    jupiter.add_moons(io)
    jupiter.add_moons(ganymede)


    jupiter.print_moons()
    mars.print_moons()
    tellus.print_moons()




if __name__=="__main__":
    main()