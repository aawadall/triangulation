"""Firefighter behaviour"""
import random
from plotter import Line

names = [
    'Abigail',
    'Alexandra',
    'Alison',
    'Amanda',
    'Amelia',
    'Amy',
    'Andrea',
    'Angela',
    'Anna',
    'Anne',
    'Audrey',
    'Ava',
    'Bella',
    'Bernadette',
    'Carol',
    'Caroline',
    'Carolyn',
    'Chloe',
    'Claire',
    'Deirdre',
    'Diana',
    'Diane',
    'Donna',
    'Dorothy',
    'Elizabeth',
    'Ella',
    'Emily',
    'Emma',
    'Faith',
    'Felicity',
    'Fiona',
    'Gabrielle',
    'Grace',
    'Hannah',
    'Heather',
    'Irene',
    'Jan',
    'Jane',
    'Jasmine',
    'Jennifer',
    'Jessica',
    'Joan',
    'Joanne',
    'Julia',
    'Karen',
    'Katherine',
    'Kimberly',
    'Kylie',
    'Lauren',
    'Leah',
    'Lillian',
    'Lily',
    'Lisa',
    'Madeleine',
    'Maria',
    'Mary',
    'Megan',
    'Melanie',
    'Michelle',
    'Molly',
    'Natalie',
    'Nicola',
    'Olivia',
    'Penelope',
    'Pippa',
    'Rachel',
    'Rebecca',
    'Rose',
    'Ruth',
    'Sally',
    'Samantha',
    'Sarah',
    'Sonia',
    'Sophie',
    'Stephanie',
    'Sue',
    'Theresa',
    'Tracey',
    'Una',
    'Vanessa',
    'Victoria',
    'Virginia',
    'Wanda',
    'Wendy',
    'Yvonne',
    'Zoe',
    'Adam',
    'Adrian',
    'Alan',
    'Alexander',
    'Andrew',
    'Anthony',
    'Austin',
    'Benjamin',
    'Blake',
    'Boris',
    'Brandon',
    'Brian',
    'Cameron',
    'Carl',
    'Charles',
    'Christian',
    'Christopher',
    'Colin',
    'Connor',
    'Dan',
    'David',
    'Dominic',
    'Dylan',
    'Edward',
    'Eric',
    'Evan',
    'Frank',
    'Gavin',
    'Gordon',
    'Harry',
    'Ian',
    'Isaac',
    'Jack',
    'Jacob',
    'Jake',
    'James',
    'Jason',
    'Joe',
    'John',
    'Jonathan',
    'Joseph',
    'Joshua',
    'Julian',
    'Justin',
    'Keith',
    'Kevin',
    'Leonard',
    'Liam',
    'Lucas',
    'Luke',
    'Matt',
    'Max',
    'Michael',
    'Nathan',
    'Neil',
    'Nicholas',
    'Oliver',
    'Owen',
    'Paul',
    'Peter',
    'Phil',
    'Piers',
    'Richard',
    'Robert',
    'Ryan',
    'Sam',
    'Sean',
    'Sebastian',
    'Simon',
    'Stephen',
    'Steven',
    'Stewart',
    'Thomas',
    'Tim',
    'Trevor',
    'Victor',
    'Warren',
    'William']


class Firefighter(object):
    def __init__(self, location=[0, 0, 0], name=None, bounds=None, max_v=1, beta=0.99):
        self.location = location
        self.x_trail = [location[0]]
        self.y_trail = [location[1]]
        self.z_trail = [location[2]]
        if name is None:
            self.name = ''.join(random.choice(names))
        else:
            self.name = name
        self.velocity = [0.0, 0.0, 0.0]
        self.max_v = max_v
        self.beta = beta
        #@todo add health metrics
        #@body define how health metrics are to be stored per firefighter,
        # and decide if it is stored in a separate object or under the main Firefighter object
        self.bounds = bounds

    def random_walk(self):
        """random walk firefighter with random values"""
        random_step = [(random.random() - 0.5) * 2 * self.max_v for _ in range(3)]
        self.velocity = [self.beta * self.velocity[idx] + (1-self.beta) * random_step[idx] for idx in range(3)]
        self.location = [self.location[idx] + self.velocity[idx] for idx in range(3)]
        if self.bounds is not None:
            for idx in range(3):
                if self.location[idx] < 0:
                    self.location[idx] = 0
                if self.location[idx] > self.bounds[idx]:
                    self.location[idx] = self.bounds[idx]
        self.x_trail.append(self.location[0])
        self.y_trail.append(self.location[1])
        self.z_trail.append(self.location[2])

    def draw(self):
        return Line(self.x_trail,
                    self.y_trail,
                    self.z_trail,
                    'green')

