from union_find_algorithm import initialize, find, union, are_in_same_group
import unittest
import time

class TestUnionFind(unittest.TestCase):
    def setUp(self):
        """ Ky funksion ekzekutohet para çdo testi. Inicializon perdoruesit. """
        self.num_users = 5
        self.parent, self.rank = initialize(self.num_users)

    def test_initialization(self):
        """ Teston nese inicializimi i struktures eshte korrekt. """
        expected_parent = [i for i in range(self.num_users)]
        expected_rank = [0] * self.num_users
        self.assertEqual(self.parent, expected_parent)
        self.assertEqual(self.rank, expected_rank)

    def test_union(self):
        """ Teston nese funksioni union bashkon sakte dy perdorues. """
        union(self.parent, self.rank, 0, 1)
        self.assertTrue(are_in_same_group(self.parent, 0, 1))

    def test_find_path_compression(self):
        """ Teston nese kompresimi i shtegut funksionon sakte. """
        union(self.parent, self.rank, 0, 1)
        union(self.parent, self.rank, 1, 2)
        find(self.parent, 2)  # Kjo duhet te optimizoje strukturen
        self.assertEqual(find(self.parent, 0), find(self.parent, 2))

    def test_disconnected_users(self):
        """ Teston nese perdoruesit e pashoqeruar nuk jane ne te njejtin grup. """
        self.assertFalse(are_in_same_group(self.parent, 0, 2))
        union(self.parent, self.rank, 0, 1)
        self.assertFalse(are_in_same_group(self.parent, 0, 2))

    def test_small_network(self):
        """Testim me nje rrjet te vogel prej 5 perdoruesish."""
        parent, rank = initialize(5)
        union(parent, rank, 0, 1)
        self.assertTrue(are_in_same_group(parent, 0, 1))
        self.assertFalse(are_in_same_group(parent, 0, 2))

    def test_single_user(self):
        """Testim kur kemi vetem nje perdorues."""
        parent, rank = initialize(1)
        self.assertTrue(are_in_same_group(parent, 0, 0))  # Perdoruesi eshte vetja e tij

    def test_large_network(self):
        """Testim me nje rrjet te madh prej 1000 perdoruesish."""
        parent, rank = initialize(1000)
        for i in range(999):
            union(parent, rank, i, i + 1)
        self.assertTrue(are_in_same_group(parent, 0, 999))  # Te gjithe jane te lidhur

    def test_time_performance(self):
        """Matja e kohes per nje rrjet shume te madh prej 6 perdoruesish."""
        parent, rank = initialize(6)
        start_time = time.time()
        for i in range(5):
            union(parent, rank, i, i + 1)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Koha e ekzekutimit per 6 perdorues: {execution_time:.5f} sekonda")
        self.assertTrue(execution_time < 1)  # Sigurohemi qe ekzekutimi te mos zgjase shume

if __name__ == "__main__":
    unittest.main()
