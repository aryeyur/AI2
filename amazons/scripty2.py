import run_amazons
import globFile

if __name__ == '__main__':

    # simple vs selective (1-3)
    """
    globFile.glob_file.write('3 2 5 n simple_player SelectivePlayer | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'simple_player', 'SelectivePlayer').run()

    globFile.glob_file.write('3 10 5 n simple_player SelectivePlayer | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'simple_player', 'SelectivePlayer').run()

    globFile.glob_file.write('3 50 5 n simple_player SelectivePlayer | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'simple_player', 'SelectivePlayer').run()

    # selective vs simple (1-3) - 2

    globFile.glob_file.write('3 2 5 n SelectivePlayer simple_player | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'SelectivePlayer', 'simple_player').run()

    globFile.glob_file.write('3 10 5 n SelectivePlayer simple_player | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'SelectivePlayer', 'simple_player').run()

    globFile.glob_file.write('3 50 5 n SelectivePlayer simple_player | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'SelectivePlayer', 'simple_player').run()

    # simple vs improved+selective (4-6)

    globFile.glob_file.write('3 2 5 n simple_player ImprovedSelectivePlayer | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'simple_player', 'ImprovedSelectivePlayer').run()

    globFile.glob_file.write('3 10 5 n simple_player simple_player | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'simple_player', 'ImprovedSelectivePlayer').run()

    globFile.glob_file.write('3 50 5 n simple_player simple_player | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'simple_player', 'ImprovedSelectivePlayer').run()

    # improved+selective vs simple (4-6) - 2

    globFile.glob_file.write('3 2 5 n ImprovedSelectivePlayer simple_player | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'ImprovedSelectivePlayer', 'simple_player').run()

    globFile.glob_file.write('3 10 5 n ImprovedSelectivePlayer simple_player | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'ImprovedSelectivePlayer', 'simple_player').run()

    globFile.glob_file.write('3 50 5 n ImprovedSelectivePlayer simple_player | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'ImprovedSelectivePlayer', 'simple_player').run()

    # simple vs improved (7-9)

    globFile.glob_file.write('3 2 5 n simple_player ImprovedPlayer | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'simple_player', 'ImprovedPlayer').run()

    globFile.glob_file.write('3 10 5 n simple_player ImprovedPlayer | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'simple_player', 'ImprovedPlayer').run()

    globFile.glob_file.write('3 50 5 n simple_player ImprovedPlayer | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'simple_player', 'ImprovedPlayer').run()

    # improved vs simple (7-9) - 2

    globFile.glob_file.write('3 2 5 n ImprovedPlayer simple_player | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'ImprovedPlayer', 'simple_player').run()

    globFile.glob_file.write('3 10 5 n ImprovedPlayer simple_player | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'ImprovedPlayer', 'simple_player').run()

    globFile.glob_file.write('3 50 5 n ImprovedPlayer simple_player | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'ImprovedPlayer', 'simple_player').run()

    # selective vs improved (10-12)

    globFile.glob_file.write('3 2 5 n SelectivePlayer ImprovedPlayer | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'SelectivePlayer', 'ImprovedPlayer').run()

    globFile.glob_file.write('3 10 5 n SelectivePlayer ImprovedPlayer | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'SelectivePlayer', 'ImprovedPlayer').run()

    globFile.glob_file.write('3 50 5 n SelectivePlayer ImprovedPlayer | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'SelectivePlayer', 'ImprovedPlayer').run()

    # improved vs selective (10-12) - 2

    globFile.glob_file.write('3 2 5 n ImprovedPlayer SelectivePlayer | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'ImprovedPlayer', 'SelectivePlayer').run()

    globFile.glob_file.write('3 10 5 n ImprovedPlayer SelectivePlayer | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'ImprovedPlayer', 'SelectivePlayer').run()

    globFile.glob_file.write('3 50 5 n ImprovedPlayer SelectivePlayer | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'ImprovedPlayer', 'SelectivePlayer').run()

    # selective vs selective+improved (13-15)

    globFile.glob_file.write('3 2 5 n SelectivePlayer ImprovedSelectivePlayer | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'SelectivePlayer', 'ImprovedSelectivePlayer').run()
    """
    globFile.glob_file.write('3 10 5 n SelectivePlayer ImprovedSelectivePlayer | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'SelectivePlayer', 'ImprovedSelectivePlayer').run()
    """
    globFile.glob_file.write('3 50 5 n SelectivePlayer ImprovedSelectivePlayer | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'SelectivePlayer', 'ImprovedSelectivePlayer').run()

    # selective+improved vs selective (13-15) - 2

    globFile.glob_file.write('3 2 5 n ImprovedSelectivePlayer SelectivePlayer | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'ImprovedSelectivePlayer', 'SelectivePlayer').run()

    globFile.glob_file.write('3 10 5 n ImprovedSelectivePlayer SelectivePlayer | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'ImprovedSelectivePlayer', 'SelectivePlayer').run()

    globFile.glob_file.write('3 50 5 n ImprovedSelectivePlayer SelectivePlayer | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'ImprovedSelectivePlayer', 'SelectivePlayer').run()

    # improved vs selective+improved (15-18)

    globFile.glob_file.write('3 2 5 n ImprovedPlayer ImprovedSelectivePlayer | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'ImprovedPlayer', 'ImprovedSelectivePlayer').run()

    globFile.glob_file.write('3 10 5 n ImprovedPlayer ImprovedSelectivePlayer | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'ImprovedPlayer', 'ImprovedSelectivePlayer').run()

    globFile.glob_file.write('3 50 5 n ImprovedPlayer ImprovedSelectivePlayer | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'ImprovedPlayer', 'ImprovedSelectivePlayer').run()

    # selective+improved vs improved (15-18) - 2

    globFile.glob_file.write('3 2 5 n ImprovedSelectivePlayer ImprovedPlayer | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'ImprovedSelectivePlayer', 'ImprovedPlayer').run()

    globFile.glob_file.write('3 10 5 n ImprovedSelectivePlayer ImprovedPlayer | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'ImprovedSelectivePlayer', 'ImprovedPlayer').run()

    globFile.glob_file.write('3 50 5 n ImprovedSelectivePlayer ImprovedPlayer | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'ImprovedSelectivePlayer', 'ImprovedPlayer').run()
    """