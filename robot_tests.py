__author__ = 'harebenj'
from robot_positions import RobotPositionCalculationClass
import inspect

class RobotPositionTestClass():

    def run_tests(self):
        # Get all the tests in this class
        tests = inspect.getmembers(RobotPositionTestClass, predicate=inspect.ismethod)

        for test in tests:
            if test[0] == 'run_tests':
                continue
            test[1](self)

    def basic_robot_test(self):

        test_args = []
        test_args.append('5 5')
        test_args.append('1 2 N')
        test_args.append('LMLMLMLMM')
        test_args.append('3 3 E')
        test_args.append('MMRMMRMRRM')

        positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)

        assert(positions[0]) == '1 3 N'
        assert(positions[1]) == '5 1 E'

        print "Basic Robot Test Passed!"

    def advanced_robot_test(self):

        test_args = []
        test_args.append('10 10')
        test_args.append('2 3 N')
        test_args.append('RMMLMRM')
        test_args.append('9 9 E')
        test_args.append('MMRMMRMRRM')
        test_args.append('4 1 S')
        test_args.append('MMLMLMMRRM')
        test_args.append('6 1 W')
        test_args.append('MMLMRMMLMM')

        positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)

        assert(positions[0]) == '5 4 E'
        assert(positions[1]) == '10 7 E'
        assert(positions[2]) == '5 1 S'
        assert(positions[3]) == '4 0 S'

        print "Advanced Robot Test Passed!"

    def invalid_args_test_1(self):

        test_args = 123  # Args must be a list

        try:
            positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)
        except TypeError:
            print "Invalid Args Test 1 Passed!"

    def invalid_args_test_2(self):

        test_args = ['5 5', '1 2 N']  # There must be at least 3 args

        try:
            positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)
        except TypeError:
            print "Invalid Args Test 2 Passed!"

    def invalid_args_test_3(self):

        test_args = ['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E']  # There must be an odd number of args

        try:
            positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)
        except TypeError:
            print "Invalid Args Test 3 Passed!"

    def invalid_args_test_4(self):

        test_args = ['5 5', 12, 'LMLMLMLMM', '3 3 E']  # All args must be strings

        try:
            positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)
        except TypeError:
            print "Invalid Args Test 4 Passed!"

    def invalid_position_data_test_1(self):

        test_args = []
        test_args.append('-2 5')  # Upper right coordinate cannot be negative
        test_args.append('1 2 N')
        test_args.append('LMLMLMLMM')
        test_args.append('3 3 E')
        test_args.append('MMRMMRMRRM')

        try:
            positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)
        except ValueError:
            print "Invalid Position Test 1 Passed!"

    def invalid_position_data_test_2(self):

        test_args = []
        test_args.append('NOT POSITION AT ALL')  # Position data must be formatted correctly
        test_args.append('1 2 N')
        test_args.append('LMLMLMLMM')
        test_args.append('3 3 E')
        test_args.append('MMRMMRMRRM')

        try:
            positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)
        except ValueError:
            print "Invalid Position Test 2 Passed!"

    def invalid_robot_position_test_1(self):

        test_args = []
        test_args.append('5 5')
        test_args.append('1 none N')  # Robot position my be numbers
        test_args.append('LMLMLMLMM')
        test_args.append('3 3 E')
        test_args.append('MMRMMRMRRM')

        try:
            positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)
        except ValueError:
            print "Invalid Robot Position Test 1 Passed!"

    def invalid_robot_position_test_2(self):

        test_args = []
        test_args.append('5 5')
        test_args.append('1 6 N')  # Robot position cannot be outside the rectangle
        test_args.append('LMLMLMLMM')
        test_args.append('3 3 E')
        test_args.append('MMRMMRMRRM')

        try:
            positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)
        except ValueError:
            print "Invalid Robot Position Test 2 Passed!"

    def invalid_robot_position_test_3(self):

        test_args = []
        test_args.append('5 5')
        test_args.append('1 2 B')  # Robot position facing must be one of N, E, S, W
        test_args.append('LMLMLMLMM')
        test_args.append('3 3 E')
        test_args.append('MMRMMRMRRM')

        try:
            positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)
        except ValueError:
            print "Invalid Robot Position Test 3 Passed!"

    def invalid_robot_movement_test(self):

        test_args = []
        test_args.append('5 5')
        test_args.append('1 3 N')
        test_args.append('LMLMLMLMBBBBM')  # Robot movement can only contain LMR
        test_args.append('3 3 E')
        test_args.append('MMRMMRMRRM')

        try:
            positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)
        except ValueError:
            print "Invalid Robot Movement Test Passed!"

    def test_robot_hits_max_x(self):

        test_args = []
        test_args.append('5 5')
        test_args.append('1 0 E')
        test_args.append('MMMMMMM')

        positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)

        assert(positions[0]) == '5 0 E'

        print "Robot Hits Max X Test Passed!"

    def test_robot_hits_min_x(self):

        test_args = []
        test_args.append('5 5')
        test_args.append('3 0 W')
        test_args.append('MMMMMMM')

        positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)

        assert(positions[0]) == '0 0 W'

        print "Robot Hits Min X Test Passed!"

    def test_robot_hits_max_y(self):

        test_args = []
        test_args.append('5 5')
        test_args.append('0 0 N')
        test_args.append('MMMMMMM')

        positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)

        assert(positions[0]) == '0 5 N'

        print "Robot Hits Max Y Test Passed!"

    def test_robot_hits_min_y(self):

        test_args = []
        test_args.append('5 5')
        test_args.append('0 3 S')
        test_args.append('MMMMMMM')

        positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)

        assert(positions[0]) == '0 0 S'

        print "Robot Hits Min Y Test Passed!"

    def test_robot_hits_existing_robot_1(self):

        test_args = []
        test_args.append('5 5')
        test_args.append('1 3 S')
        test_args.append('MMMMMMM')  # This will intersect with the below robot at 1, 1, stopping it
        test_args.append('1 0 N')
        test_args.append('LM')

        positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)

        assert(positions[0]) == '1 1 S'
        assert(positions[1]) == '0 0 W'

        print "Robot Hits Existing Robot Test 1 Passed!"

    def test_robot_hits_existing_robot_2(self):

        test_args = []
        test_args.append('5 5')
        test_args.append('3 3 S')
        test_args.append('MMMMMMM')
        test_args.append('0 0 E')
        test_args.append('MMMMMMM')  # This will intersect the above robot after it has moved to 3, 0, stopping it

        positions = RobotPositionCalculationClass().calculate_robot_positions(test_args)

        assert(positions[0]) == '3 0 S'
        assert(positions[1]) == '2 0 E'

        print "Robot Hits Existing Robot Test 2 Passed!"