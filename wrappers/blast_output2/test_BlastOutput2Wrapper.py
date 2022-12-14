import unittest

import json

from wrappers.blast_output2.BlastOutput2Wrapper import BlastOutput2Wrapper


examples_directory_path = 'wrappers/blast_output2/example_blast_output2s/'

with open(examples_directory_path + 'unkeyed.json', 'r') as f:
    unkeyed = json.loads(f.read())

with open(examples_directory_path + 'keyed.json', 'r') as f:
    keyed = json.loads(f.read())

with open(examples_directory_path + 'zero_reports.json', 'r') as f:
    zero_reports = json.loads(f.read())


class TestBlastOutput2Property(unittest.TestCase):
    def test_unkeyed(self):
        blast_output2 = BlastOutput2Wrapper(unkeyed)
        self.assertIs(blast_output2.blast_output2, unkeyed)

    def test_keyed(self):
        blast_output2 = BlastOutput2Wrapper(keyed)
        self.assertIs(blast_output2.blast_output2, keyed['BlastOutput2'])


class TestReportsGetter(unittest.TestCase):
    def test_unkeyed(self):
        blast_output2 = BlastOutput2Wrapper(unkeyed)
        reports = blast_output2.reports
        self.assertEqual(len(reports), 2)
        report1 = reports[0]
        report2 = reports[1]
        # just check some report values
        query_from1 = report1.results.search.hits[0].hsps[0].query_from
        self.assertEqual(query_from1, 561)
        hit_from2 = report2.results.search.hits[0].hsps[0].hit_from
        self.assertEqual(hit_from2, 790)

    def test_keyed(self):
        blast_output2 = BlastOutput2Wrapper(keyed)
        reports = blast_output2.reports
        self.assertEqual(len(reports), 2)
        report1 = reports[0]
        report2 = reports[1]
        # just check some report values
        query_to1 = report1.results.search.hits[0].hsps[0].query_to
        self.assertEqual(query_to1, 2013)
        hit_from2 = report2.results.search.hits[0].hsps[0].hit_from
        self.assertEqual(hit_from2, 1223)

    def test_zero_reports(self):
        blast_output2 = BlastOutput2Wrapper(zero_reports)
        reports = blast_output2.reports
        self.assertEqual(len(reports), 0)
