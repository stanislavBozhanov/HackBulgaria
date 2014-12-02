class Dungeon():
    def __init__(self, filepath):
        self.filepath = filepath
        self.set_dungeon_map(filepath)

    def _set_dungeon_map(self, filepath):
        my_file = open(self.filepath, 'r')
        content = my_file.read()
        content = content.split('\n')
        self.dungeon_map = content

    def print_map(self):
        for row in self.dungeon_map:
            print(row)

    def spawn(player_name, entity):
        pass


# def main():
#     dun = Dungeon('basic_dungeon.txt')
#     dun.print_map()


# if __name__ == '__main__':
#     main()
