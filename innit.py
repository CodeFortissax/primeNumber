class Dog:
    def __init__(self, dogBreed, dogEyeColor, dogOwner):
        self.breed = dogBreed
        self.eyeColor = dogEyeColor
        self.owner = dogOwner


tomita = Dog("Fox Terrier", "brown", "Polly")


print("This dog is a", tomita.breed, "and his eyes are", tomita.eyeColor, "and it belongs to", tomita.owner)


class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something


class B(A):
    def __init__(self, something):
        # Calling init of parent class
        A.__init__(self, something)
        print("B init called")
        self.something = something


obj = B("NOTHING")