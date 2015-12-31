import run_amazons
import globFile

if __name__ == '__main__':

    # simple vs selective 0.05


    globFile.glob_file.write('3 2 5 n simple_player SelectivePlayer 0 0.05 | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'simple_player', 'SelectivePlayer', 0, 0.05).run()

    globFile.glob_file.write('3 10 5 n simple_player SelectivePlayer 0 0.05 | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'simple_player', 'SelectivePlayer', 0, 0.05).run()

    globFile.glob_file.write('3 50 5 n simple_player SelectivePlayer 0 0.05 | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'simple_player', 'SelectivePlayer', 0, 0.05).run()

    # selective 0.05 vs simple

    globFile.glob_file.write('3 2 5 n SelectivePlayer simple_player 0.05 0 | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'SelectivePlayer', 'simple_player', 0.05, 0).run()

    globFile.glob_file.write('3 10 5 n SelectivePlayer simple_player 0.05 0 | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'SelectivePlayer', 'simple_player', 0.05, 0).run()

    globFile.glob_file.write('3 50 5 n SelectivePlayer simple_player 0.05 0 | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'SelectivePlayer', 'simple_player', 0.05, 0).run()

    # simple vs selective 0.2

    globFile.glob_file.write('3 2 5 n simple_player SelectivePlayer 0 0.2 | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'simple_player', 'SelectivePlayer', 0, 0.2).run()

    globFile.glob_file.write('3 10 5 n simple_player SelectivePlayer 0 0.2 | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'simple_player', 'SelectivePlayer', 0, 0.2).run()

    globFile.glob_file.write('3 50 5 n simple_player SelectivePlayer 0 0.2 | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'simple_player', 'SelectivePlayer', 0, 0.2).run()

    # selective 0.2 vs simple

    globFile.glob_file.write('3 2 5 n SelectivePlayer simple_player 0.2 0 | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'SelectivePlayer', 'simple_player', 0.2, 0).run()

    globFile.glob_file.write('3 10 5 n SelectivePlayer simple_player 0.2 0 | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'SelectivePlayer', 'simple_player', 0.2, 0).run()

    globFile.glob_file.write('3 50 5 n SelectivePlayer simple_player 0.2 0 | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'SelectivePlayer', 'simple_player', 0.2, 0).run()

    # simple vs selective 0.7

    globFile.glob_file.write('3 2 5 n simple_player SelectivePlayer 0 0.7 | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'simple_player', 'SelectivePlayer', 0, 0.7).run()

    globFile.glob_file.write('3 10 5 n simple_player SelectivePlayer 0 0.7 | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'simple_player', 'SelectivePlayer', 0, 0.7).run()

    globFile.glob_file.write('3 50 5 n simple_player SelectivePlayer 0 0.7 | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'simple_player', 'SelectivePlayer', 0, 0.7).run()

    # selective 0.7 vs simple

    globFile.glob_file.write('3 2 5 n SelectivePlayer simple_player 0.7 0 | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'SelectivePlayer', 'simple_player', 0.7, 0).run()

    globFile.glob_file.write('3 10 5 n SelectivePlayer simple_player 0.7 0 | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'SelectivePlayer', 'simple_player', 0.7, 0).run()

    globFile.glob_file.write('3 50 5 n SelectivePlayer simple_player 0.7 0 | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'SelectivePlayer', 'simple_player', 0.7, 0).run()

    # selective 0.2 vs selective 0.05

    globFile.glob_file.write('3 2 5 n SelectivePlayer SelectivePlayer 0.2 0.05 | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.2, 0.05).run()

    globFile.glob_file.write('3 10 5 n SelectivePlayer SelectivePlayer 0.2 0.05 | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.2, 0.05).run()

    globFile.glob_file.write('3 50 5 n SelectivePlayer SelectivePlayer 0.2 0.05 | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.2, 0.05).run()

    # selective 0.05 vs selective 0.2

    globFile.glob_file.write('3 2 5 n SelectivePlayer SelectivePlayer 0.05 0.2 | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.05, 0.2).run()

    globFile.glob_file.write('3 10 5 n SelectivePlayer SelectivePlayer 0.05 0.2 | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.05, 0.2).run()

    globFile.glob_file.write('3 50 5 n SelectivePlayer SelectivePlayer 0.05 0.2 | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.05, 0.2).run()

    # selective 0.2 vs selective 0.7

    globFile.glob_file.write('3 2 5 n SelectivePlayer SelectivePlayer 0.2 0.7 | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.2, 0.7).run()

    globFile.glob_file.write('3 10 5 n SelectivePlayer SelectivePlayer 0.2 0.7 | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.2, 0.7).run()

    globFile.glob_file.write('3 50 5 n SelectivePlayer SelectivePlayer 0.2 0.7 | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.2, 0.7).run()

    # selective 0.7 vs selective 0.2

    globFile.glob_file.write('3 2 5 n SelectivePlayer SelectivePlayer 0.7 0.2 | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.7, 0.2).run()

    globFile.glob_file.write('3 10 5 n SelectivePlayer SelectivePlayer 0.7 0.2 | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.7, 0.2).run()

    globFile.glob_file.write('3 50 5 n SelectivePlayer SelectivePlayer 0.7 0.2 | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.7, 0.2).run()

    # selective 0.7 vs selective 0.05

    globFile.glob_file.write('3 2 5 n SelectivePlayer SelectivePlayer 0.7 0.05 | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.7, 0.05).run()

    globFile.glob_file.write('3 10 5 n SelectivePlayer SelectivePlayer 0.7 0.05 | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.7, 0.05).run()

    globFile.glob_file.write('3 50 5 n SelectivePlayer SelectivePlayer 0.7 0.05 | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.7, 0.05).run()

    # selective 0.05 vs selective 0.7

    globFile.glob_file.write('3 2 5 n SelectivePlayer SelectivePlayer 0.05 0.7 | ')
    run_amazons.amazonsRunner(3, 2, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.05, 0.7).run()

    globFile.glob_file.write('3 10 5 n SelectivePlayer SelectivePlayer 0.05 0.7 | ')
    run_amazons.amazonsRunner(3, 10, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.05, 0.7).run()

    globFile.glob_file.write('3 50 5 n SelectivePlayer SelectivePlayer 0.05 0.7 | ')
    run_amazons.amazonsRunner(3, 50, 5, 'n', 'SelectivePlayer', 'SelectivePlayer', 0.05, 0.7).run()
