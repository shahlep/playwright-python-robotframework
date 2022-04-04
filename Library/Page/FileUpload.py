from robot.api.deco import library, keyword


@library
class FileChooser:
    upload_element_locator = "input[name=\"file\"]"
    upload_button = "input:has-text(\"Upload\")"
    uploaded_file_locator = "#uploaded-files"
    file_to_upload = None

    @keyword
    def silently_upload_file(self,page, filepath):
        page.set_input_files(FileChooser.upload_element_locator, filepath)
        page.click(FileChooser.upload_button)

    @keyword
    def click_on_file_upload(self,page):
        page.click(FileChooser.upload_element_locator)
        page.click(FileChooser.upload_button)

    @keyword
    def set_filepath_upload(self,filepath):
        FileChooser.file_to_upload = filepath

    @keyword
    def get_uploaded_file_name(self,page):
        element = page.query_selector(FileChooser.uploaded_file_locator)
        return element.text_content()
