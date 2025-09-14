from unittest import TestCase
from fastapi.testclient import TestClient
from flexibill.app.application import create_application


class TestBaseEventHandler(TestCase):
    def test_startup_handler(self):
        app = create_application()
        with self.assertLogs('flexibill', level='INFO') as cm:

            with TestClient(app):
                pass
            self.assertEqual(cm.output,
                             ['INFO:flexibill:Starting up ...',
                              'INFO:flexibill:Shutting down ...'])
