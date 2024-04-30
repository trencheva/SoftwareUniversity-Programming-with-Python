from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self) -> None:
        self.platform = SocialMedia('Anton', 'Instagram', 10, 'comedy')

    def test_correct_init(self):
        self.assertEqual('Anton', self.platform._username)
        self.assertEqual('Instagram', self.platform._platform)
        self.assertEqual(10, self.platform._followers)
        self.assertEqual('comedy', self.platform._content_type)
        self.assertEqual([], self.platform._posts)

    def test_validate_and_set_pl_With_non_allowed_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.platform2 = SocialMedia('Anton', 'In', 10, 'comedy')
        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_followers_under_10_raises_ve(self):
        with self.assertRaises(ValueError) as ve:

            self.platform.followers = -2
        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_create_post_expect_success(self):
        result = self.platform.create_post('asd')
        self.assertEqual(f"New comedy post created by Anton on Instagram.", result)
        self.assertEqual([{'content': 'asd', 'likes': 0, 'comments': []}], self.platform._posts)

    def test_like_post_with_index_less_than_0(self):
        result = self.platform.like_post(-2)
        self.assertEqual("Invalid post index.", result)

    def test_like_post_with_index_higher_than_len(self):
        result = self.platform.like_post(200)
        self.assertEqual("Invalid post index.", result)

    def test_like_post_valid_index_post_likes_less_than_10(self):
        self.platform.create_post('abcde')
        result = self.platform.like_post(0)
        self.assertEqual(1, self.platform._posts[0]['likes'])
        self.assertEqual("Post liked by Anton.", result)

    def test_like_post_valid_index_post_likes_greather_than_max(self):
        self.platform.create_post('abcde')
        self.platform._posts[0]['likes'] = 10
        result = self.platform.like_post(0)
        self.assertEqual(10, self.platform._posts[0]['likes'])
        self.assertEqual("Post has reached the maximum number of likes.", result)

    def test_comment_on_post_valid_len(self):
        self.platform.create_post('today is great day')
        result = self.platform.comment_on_post(0, 'its great ,tatataat')
        self.assertEqual("Comment added by Anton on the post.", result)
        self.assertEqual([{'user': 'Anton', 'comment': 'its great ,tatataat'}], self.platform._posts[0]['comments'])

    def test_comment_less_symbols(self):
        self.platform.create_post('today is great day')
        result = self.platform.comment_on_post(0, 'its')

        self.assertEqual("Comment should be more than 10 characters.", result)

if __name__ == '__main__':
    main()