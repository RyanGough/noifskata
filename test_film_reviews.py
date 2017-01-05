import unittest
import film_reviews 

class TestFilmReviews(unittest.TestCase):

    def test_classify_filmsonline_bad(self):
        review = "this is a really gnarly film,ryan gough,49,sharknado"
        self.assertEqual(film_reviews.review("filmsonline", review), "bad")

    def test_classify_filmsonline_good(self):
        review = "this is a really great film,ryan gough,51,sharknado 2"
        self.assertEqual(film_reviews.review("filmsonline", review), "good")

    def test_classify_filmorama_bad(self):
        review = "the piano,jayd lawrence,film sucks bro,2"
        self.assertEqual(film_reviews.review("filmorama", review), "bad")

    def test_classify_filmorama_good(self):
        review = "the piano,paul chedd,film rules bro,3"
        self.assertEqual(film_reviews.review("filmorama", review), "good")

    def test_classify_filmorama_malformed(self):
        review = "robin hood - prince of thieves,ryan gough,best film ever obvs.,null"
        self.assertEqual(film_reviews.review("filmorama", review), "error")

    def test_classify_rottenfruit_good(self):
        review = "****,will hunt,i liked this film,transformers"
        self.assertEqual(film_reviews.review("rottenfruit", review), "good")

    def test_classify_rottenfruit_bad(self):
        review = "***,will hunt,i hated this film,transformers 2"
        self.assertEqual(film_reviews.review("rottenfruit", review), "bad")

    def test_classify_rottenfruit_bad_adjusted_for_warren(self):
        review = "***,warren bew,meh,transformers 2"
        self.assertEqual(film_reviews.review("rottenfruit", review), "good")

    def test_classify_rottenfruit_bad_adjusted_for_warren(self):
        review = "***,warren bew,meh,transformers 2"
        self.assertEqual(film_reviews.review("rottenfruit", review), "good")

    def test_classify_filmsonline_bad_in_french(self):
        review = "this is a really gnarly film,ryan gough,49,sharknado"
        self.assertEqual(film_reviews.review("filmsonline", review, True), "merde")

    def test_classify_filmsonline_good_in_french(self):
        review = "this is a really great film,ryan gough,51,sharknado 2"
        self.assertEqual(film_reviews.review("filmsonline", review, True), "tres bon")

    def test_classify_filmorama_bad_in_french(self):
        review = "the piano,jayd lawrence,film sucks bro,2"
        self.assertEqual(film_reviews.review("filmorama", review, True), "merde")

    def test_classify_filmorama_good(self):
        review = "the piano,paul chedd,film rules bro,3"
        self.assertEqual(film_reviews.review("filmorama", review, True), "tres bon")

    def test_classify_rottenfruit_good_in_french(self):
        review = "****,will hunt,i liked this film,transformers"
        self.assertEqual(film_reviews.review("rottenfruit", review, True), "tres bon")

    def test_classify_rottenfruit_bad_in_french(self):
        review = "***,will hunt,i hated this film,transformers 2"
        self.assertEqual(film_reviews.review("rottenfruit", review, True), "merde")

    def test_classify_unknown_source(self):
        review = "A+,neal baker,damn good,the quiet man"
        self.assertEqual(film_reviews.review("webfilms", review, True), "error")


if __name__ == '__main__':
    unittest.main()
