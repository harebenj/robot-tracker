__author__ = 'harebenj'
import re


class RobotPositionCalculationClass():

    x_max = 0
    y_max = 0
    directions = ['N', 'E', 'S', 'W']
    robots_info = []

    def calculate_robot_positions(self, args):

        # Check that the input is a list of strings as required (if it isn't a list, it'll error with a TypeError too)
        if not all(isinstance(arg, basestring) for arg in args):
            raise TypeError

        # Check that the input is at least three (the minimum for position, robot position, and robot movement
        # for one robot) and odd (position + robot position and robot movement for each robot)
        if len(args) < 3 or len(args) % 2 != 1:
            raise TypeError

        position_data = args[0]
        self.calculate_area(position_data)

        self.parse_robot_info(args)

        final_positions = []
        for robot_info in self.robots_info:
            self.calculate_robot_position(robot_info)
            final_positions.append(robot_info['x_pos'] + ' ' + robot_info['y_pos'] + ' ' + robot_info['facing'])

        return final_positions

    def calculate_robot_position(self, robot_info):

        x_pos = int(robot_info['x_pos'])
        y_pos = int(robot_info['y_pos'])
        robot_id = int(robot_info['id'])
        facing = self.directions.index(robot_info['facing'])

        for command in robot_info['movement']:
            if command == 'L':
                # Using the index of self.directions to figure out which way it's facing
                facing = (facing - 1) % 4
            elif command == 'R':
                facing = (facing + 1) % 4
            else:
                if facing == 0:
                    if self.try_position(x_pos, y_pos+1, robot_id):
                        y_pos = y_pos + 1
                elif facing == 1:
                    if self.try_position(x_pos+1, y_pos, robot_id):
                        x_pos = x_pos + 1
                elif facing == 2:
                    if self.try_position(x_pos, y_pos-1, robot_id):
                        y_pos = y_pos - 1
                else:
                    if self.try_position(x_pos-1, y_pos, robot_id):
                        x_pos = x_pos - 1

        robot_info['x_pos'] = str(x_pos)
        robot_info['y_pos'] = str(y_pos)
        robot_info['facing'] = self.directions[facing]

    def try_position(self, x_pos, y_pos, robot_id):
        # Try to determine if the position is allowed, if not the robot will not move

        # First check if the robot is off the edge of the rectangle
        if x_pos < 0 or x_pos > self.x_max:
            return False
        elif y_pos < 0 or y_pos > self.y_max:
            return False

        # Now check to see if that position is occupied by any other robot
        for robot_info in self.robots_info:
            if robot_info['id'] == robot_id:
                # Don't check a robot against itself
                continue
            if x_pos == int(robot_info['x_pos']) and y_pos == int(robot_info['y_pos']):
                return False

        # Redundant but eh, makes it clearer that the square is possible
        return True

    def parse_robot_info(self, args):
        # This is both to put the information in an easier to process format and to
        # check that all the data is valid before beginning to calculate
        robots_info = []

        for i in range(1, len(args), 2):
            robot_position = args[i]
            robot_movement = args[i+1]

            robot_info = {}
            expression = re.compile('^(\d+) (\d+) ([NESW])')
            match = expression.match(robot_position)
            if match is not None:
                if int(match.group(1)) > self.x_max or int(match.group(2)) > self.y_max:
                    # Robot position is above the max allowed value
                    raise ValueError
                robot_info['id'] = i/2
                robot_info['x_pos'] = match.group(1)
                robot_info['y_pos'] = match.group(2)
                robot_info['facing'] = match.group(3)
            else:
                # Robot position is in the wrong format
                raise ValueError

            expression = re.compile('^[LRM]+$')
            match = expression.match(robot_movement)
            if match is None:
                # Robot movement is in the wrong format
                raise ValueError
            else:
                robot_info['movement'] = robot_movement

            robots_info.append(robot_info)

        self.robots_info = robots_info

    def calculate_area(self, position_data):
        expression = re.compile('^(\d+) (\d+)$')
        match = expression.match(position_data)
        if match is not None:
            self.x_max = int(match.group(1))
            self.y_max = int(match.group(2))
        else:
            # Position Data not in expected format
            raise ValueError