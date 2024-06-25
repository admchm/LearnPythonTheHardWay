from ex50 import Person

def test_combat():
    boxer = Person("Boxer", 100, 10)
    zombie = Person("Zed", 1000, 1000)

    # these asserts are bad, fix them
    assert boxer.hp == 100, "Boxer has wrong hp."
    assert zombie.hp == 1000, "Zombe has wrong hp."

    boxer.hit(zombie)
    assert zombie.alive(), "Zombie should be alive."

    zombie.hit(boxer)
    assert not boxer.alive(), "Boxer should be dead."
    
# pytest --cov="/Users/adamc/LearnPythonTheHardWay/subprojects/50_Automated_Testing"
# pytest --cov-report html:coverage --cov=.

# Another very useful thing is to add an __invariant__ function to the 
# Person class. This comes from a style of programming called Design by 
# Contract created by Bertrand Meyer where you add instrumentation to 
# your code that confirms things are working as expected. The 
# __invariant__ function's job is to check the Person object's internal 
# state and make sure that there are no "bad" conditions. For example, 
# it would confirm that self.damage is never 0 and that the person is 
# alive() when self.hp > 0. Write an __invariant__ function that your 
# test can call which uses assert to validate the Person object's 
# internal state for the test.
