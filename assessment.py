"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Polymorphism:
    Being able to use the same methods on all instances of the class and subclasses in the same manner. ie: with the same number of arguments being passed in.
   Abstraction:
    Being able to use something with out knowing (or needing to know) the details of how it works. 
   Encapsulation:
    Keeping everything close to the source

2. What is a class?
    A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator.
    https://learnpythonthehardway.org/book/ex40.html


3. What is an instance attribute?
    An instance attribute is a "post-it" on the "ker-chunk".
    It is an attribute that is assigned to the object after it has been instantiated - perhaps on initialization (__init__) or later as a result of a method. An instance attribute overides any class attributes.

4. What is a method?
    A function within the class that uses the argument "self" as the first parameter.

5. What is an instance in object orientation?
    An individual occurrence of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
    A class attribute, if there is one, is assigned when an item is instantiated and no instance attribute is specified - it is a . You would use a class attribute if the same characteristics will be shared by all instances of that class or if there is no specific information available at instantiation. 
    An instance attribute is more specific - it applies to the object itself, ie a black hat, instead of just a hat.


"""

class AcademyInfo(object):

class StudentInfo(AcademyInfo):

    def __init__(self, first_name, last_name, address):
        #initialize student info attributes (instance attributes)
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Questions(AcademyInfo):

    def __init__(self, question, correct_answer):
        #initialize exam question attributes (instance attributes)
        self.question = question
        self.correct_answer = correct_answer

class Exam(AcademyInfo):

    def __init__(self, name):
        self.name = name 
        self.question = []

# class AbstractMelonOrder(object):
#  +    """Global melon orders."""
#  +
#  +    def __init__(self, species, qty, order_type, tax):
#  +        """Initialize melon order attributes."""
#  +
#  +        self.species = species
#  +        self.qty = qty
#  +        self.shipped = False
#  +        self.order_type = order_type
#  +        self.tax = tax
#  +
#  +    def get_total(self):
#  +        """Calculate price, including tax."""
#  +
#  +        if self.species.lower() == "christmas melon":
#  +            base_price = 5 * 1.5
#  +        else:
#  +            base_price = 5
#  +
#  +        if self.order_type.lower() == "international" and self.qty < 10:
#  +            flat_fee = 3
#  +        else:
#  +            flat_fee = 0
#  +
#  +        total = ((1 + self.tax) * self.qty * base_price) + flat_fee
#  +
#  +        return total
#  +
#  +    def mark_shipped(self):
#  +        """Record the fact than an order has been shipped."""
#  +
#  +        self.shipped = True
#  +
#  +
#  +class DomesticMelonOrder(AbstractMelonOrder):
#  +    """A melon order within the USA."""
#  +
#  +    def __init__(self, species, qty):
#  +        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", .08)
#  +
#  +
#  +class InternationalMelonOrder(AbstractMelonOrder):
#  +    """An international (non-US) melon order."""
#  +
#  +    def __init__(self, species, qty, country_code):
#  +        super(InternationalMelonOrder, self).__init__(species, qty, "international", .17)
#  +        self.country_code = country_code
#  +
#  +    def get_country_code(self):
#  +        """Return the country code."""
#  +
#  +        return self.country_code
#  +
#  +


# Parts 2 through 5:
# Create your classes and class methods
