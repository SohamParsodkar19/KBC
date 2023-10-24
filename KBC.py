questions = [
    [
    "Which planet is closest to the Sun?", "Venus", "Earth", "Mars", "Mercury", "None", 4
    ],
    [
    "What causes the different phases of the Moon?", "Earth's Shadow", "Changes in the Moon's Temperature", "The Moon's Orbit around the Earth", "Aliens on the Moon", "None", 3
    ],
    [
    "What is the main source of energy for our Sun?", "Nuclear Fission", "Nuclear Fusion", "Solar wind", "Geothermal heat", "None", 2
    ],
    [
    "Which planet in our solar system has the most extensive ring system?", "Saturn", "Uranus", "Neptune", "Jupiter", "None", 1
    ],
    [
    "What is the name of the largest volcano in the solar system, located on Mars?", "Mount St. Helens", " Olympus Mons", "Mount Everest", " Mauna Loa", "None", 2
    ],
    [
    "What is the Hubble Space Telescope primarily used for?", "Observing distant galaxies", "Studying black holes", "Tracking asteroids", "Exploring underwater ecosystems", "None", 1
    ],
    [
    "What is the term for the point in the sky directly above an observer's head?", "Apex", "Zenith", "Nadir", "Horizon", "None", 2
    ],
    [
    "What is the name of the phenomenon where a total solar eclipse reveals a ring of sunlight around the darkened moon?", "Solar Halo", " Solar Corona", "Solar Parallax", "Solar Mirage", "None", 2
    ],
    [
    "What is the largest moon in the solar system and a moon of Jupiter?", "Titan", "Ganymede", "Europa", "Io", "None", 2
    ],
    [
    " Which galaxy is closest to the Milky Way?", "Andromeda", "Triangulum", "M87", "Whirlpool", "None", 1
    ],
    [
    "What is the name of the process by which a star like our Sun eventually exhausts its nuclear fuel and ends its life?", "Nova", "Nebula", "Supernova", " Red Giant", "None", 4
    ],
    [
    "Which famous spacecraft, launched in 1977, is now in interstellar space and carries a Golden Record with sounds and images from Earth?", "Voyager 1", "Apollo 11", "Hubble", "Cassini", "None", 1
    ],
    [
    "What is the term for the theoretical boundary around a black hole beyond which nothing can escape, not even light?", "Event Horizon", "Photon Sphere", "Schwarzschild Radius", "Accretion Disk", "None", 1
    ],
    [
    "Which famous astronomer developed the three laws of planetary motion that describe the motion of planets in our solar system?", "Johannes Kepler", " Galileo Galilei", "Isaac Newton", "Edwin Hubble", "None", 1
    ],
    [
    "What is the name of the most abundant element in the universe?", "Hydrogen", "Helium", "Oxygen", "Carbon", "None", 1
    ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0

for i in range(0,len(questions)):
    
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {question[1]}             b. {question[2]} ")
    print(f"c. {question[3]}             d. {question[4]} ")
    reply = int(input("Enter your answer (1-4):  or 0 to quit:"))
    if (reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        print("\n------------------------------------------------------------------------\n")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            moeny = 10000000    
    else:
        print("Wrong answer")
        break 
print(f"Your Have won {money}")    
