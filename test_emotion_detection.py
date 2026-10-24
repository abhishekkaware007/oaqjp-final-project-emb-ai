"""
Unit tests for the EmotionDetection package using unittest and unittest.mock.
Simulates Watson NLP responses to test anger, disgust, fear, joy, sadness,
and HTTP 400 / blank input handling without accessing the external endpoint.
"""
import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """
    Test suite verifying dominant emotions and error handling in emotion_detector.
    """

    @patch('requests.post')
    def test_emotion_detector(self, mock_post):
        """
        Tests the 5 core Coursera statements for dominant emotions:
        joy, anger, disgust, sadness, and fear.
        """
        mock_emotions = {
            'I am glad this happened': {
                'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.95, 'sadness': 0.02
            },
            'I am really mad about this': {
                'anger': 0.95, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.02
            },
            'I feel disgusted just hearing about this': {
                'anger': 0.01, 'disgust': 0.95, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.02
            },
            'I am so sad about this': {
                'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.01, 'sadness': 0.95
            },
            'I am really afraid that this will happen': {
                'anger': 0.01, 'disgust': 0.01, 'fear': 0.95, 'joy': 0.01, 'sadness': 0.02
            }
        }

        def mock_request(url, json, headers):
            del url, headers  # Unused in mock
            text = json['raw_document']['text']
            resp = MagicMock()
            resp.status_code = 200
            resp.json.return_value = {
                'emotionPredictions': [{'emotion': mock_emotions[text]}]
            }
            return resp

        mock_post.side_effect = mock_request

        # Test 1: Joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test 2: Anger
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test 3: Disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test 4: Sadness
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test 5: Fear
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

    @patch('requests.post')
    def test_status_400_and_blank_input(self, mock_post):
        """
        Tests HTTP 400 error handling for blank/invalid input.
        Verifies all emotions and dominant_emotion return None.
        """
        mock_resp = MagicMock()
        mock_resp.status_code = 400
        mock_post.return_value = mock_resp

        result = emotion_detector('')
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])


if __name__ == '__main__':
    unittest.main()
