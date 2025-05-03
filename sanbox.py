import time
import ujson
import urequests as requests

class PicoError(Exception):

    pass

class NetworkClient:
    def __init__(self):

        self.https_status = {200: "OK", 201: "Created"}

    def safe_post_with_retry(
        self,
        url: str,
        headers: dict,
        data: dict,
        retries: int = 3,
        timeout: int = 5,
        backoff: float = 2.0
    ) -> str:

        for attempt in range(retries):
            try:

                response = self._do_post(url, headers, data, timeout)


                self._validate_status(response.status_code)


                return self._extract_response(response)

            except Exception as e:

                if attempt == retries - 1:
                    raise PicoError(f"POST failed after {retries} attempts") from e


                wait = backoff ** attempt
                print(f"[Retry {attempt+1}] Error: {e} — waiting {wait}s before retry...")
                time.sleep(wait)

    def _do_post(self, url, headers, data, timeout):

        try:
            return requests.post(
                url,
                headers=headers,
                data=ujson.dumps(data),
                timeout=timeout
            )
        except Exception as e:
            raise PicoError(f"Network error during POST: {e}") from e

    def _validate_status(self, status: int):

        if status not in self.https_status:
            raise PicoError(f"Unexpected HTTP status: {status}")

    def _extract_response(self, response):

        try:
            return response.text
        finally:
            response.close()
