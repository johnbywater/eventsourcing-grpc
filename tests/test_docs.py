import os
import sys
from os.path import dirname, join

# from subprocess import PIPE, STDOUT
from subprocess import Popen, TimeoutExpired
from tempfile import NamedTemporaryFile
from unittest.case import TestCase

import eventsourcing_grpc

base_dir = dirname(dirname(os.path.abspath(eventsourcing_grpc.__file__)))


class TestDocs(TestCase):
    def test_readme(self):  # type: ignore
        self._out = ""

        path = join(base_dir, "README.md")
        if not os.path.exists(path):
            self.skipTest("Skipped test, README file not found: {}".format(path))

        try:
            self.check_code_snippets_in_file(path)
        finally:
            if os.path.exists("dog-school.db"):
                os.remove("dog-school.db")

        # path = join(base_dir, "README_example_with_axon.md")
        # if not os.path.exists(path):
        #     self.skipTest("Skipped test, README file not found: {}".format(path))
        # self.check_code_snippets_in_file(path)

    def test_docs(self):  # type: ignore

        skipped = [
            # 'deployment.rst'
        ]

        self._out = ""
        docs_path = os.path.join(base_dir, "docs")

        if not os.path.exists(docs_path):
            self.skipTest("Skipped test, docs folder not found: {}".format(docs_path))

        file_paths = []
        for dirpath, _, filenames in os.walk(docs_path):
            for name in filenames:
                if name in skipped:
                    continue
                if name.endswith(".rst"):
                    # if (
                    #     name.endswith("persistence.rst")
                    #     or name.endswith("domain.rst")
                    #       or name.endswith("application.rst")
                    #     or name.endswith("system.rst")
                    #     or name.endswith("examples.rst")
                    # ):
                    # if name.endswith('quick_start.rst'):
                    # if name.endswith('aggregates_in_ddd.rst'):
                    # if name.endswith('example_application.rst'):
                    # if name.endswith('everything.rst'):
                    # if name.endswith('infrastructure.rst'):
                    # if name.endswith('application.rst'):
                    # if name.endswith('snapshotting.rst'):
                    # if name.endswith('notifications.rst'):
                    # if name.endswith('projections.rst'):
                    # if name.endswith('deployment.rst'):
                    # if name.endswith('process.rst'):
                    file_paths.append(os.path.join(docs_path, dirpath, name))

        file_paths = sorted(file_paths)
        failures = []
        passed = []
        failed = []
        print("Testing code snippets in docs:")
        for path in file_paths:
            print(path)
        print("")
        for path in file_paths:
            # print("Testing code snippets in file: {}".format(path))
            try:
                self.check_code_snippets_in_file(path)
            except self.failureException as e:
                failures.append(e)
                failed.append(path)
                print(str(e).strip("\n"))
                print("FAIL")
                print("")
            else:
                passed.append(path)
                print("PASS")
                print("")
            finally:
                pass
                # self.clean_env()

        print("{} failed, {} passed".format(len(failed), len(passed)))

        if failures:
            raise failures[0]

    def check_code_snippets_in_file(self, doc_path):  # type: ignore  # noqa: C901
        # Extract lines of Python code from the README.md file.

        lines = []
        num_code_lines = 0
        num_code_lines_in_block = 0
        is_code = False
        is_md = False
        is_rst = False
        last_line = ""
        is_literalinclude = False
        module = ""
        with open(doc_path) as doc_file:
            for line_index, orig_line in enumerate(doc_file):
                # print("Line index:", line_index)
                # print("Orig line:", orig_line)
                # print("Last line:", last_line)

                line = orig_line.strip("\n")
                if line.startswith("```python"):
                    # Start markdown code block.
                    if is_rst:
                        self.fail(
                            "Markdown code block found after restructured text block "
                            "in same file."
                        )
                    is_code = True
                    is_md = True
                    line = ""
                    num_code_lines_in_block = 0
                elif is_code and is_md and line.startswith("```"):
                    # Finish markdown code block.
                    if not num_code_lines_in_block:
                        self.fail(f"No lines of code in block: {line_index + 1}")
                    is_code = False
                    line = ""
                elif is_code and is_rst and line.startswith("```"):
                    # Can't finish restructured text block with markdown.
                    self.fail(
                        "Restructured text block terminated with markdown format '```'"
                    )
                elif line.startswith(".. code-block:: python") or (
                    line.strip() == ".." and "include-when-testing" in last_line
                ):
                    # Start restructured text code block.
                    if is_md:
                        self.fail(
                            "Restructured text code block found after markdown block "
                            "in same file."
                        )
                    is_code = True
                    is_rst = True
                    line = ""
                    num_code_lines_in_block = 0
                elif line.startswith(".. literalinclude::"):
                    is_literalinclude = True
                    module = line.strip().split(" ")[-1]  # get the file path
                    module = module[:-3]  # remove the '.py' from the end
                    module = module.lstrip("./")  # remove all the ../../..
                    module = module.replace("/", ".")  # swap dots for slashes
                    line = ""

                elif is_literalinclude:
                    if "pyobject" in line:
                        # Assume ".. literalinclude:: ../../xxx/xx.py"
                        # Or ".. literalinclude:: ../xxx/xx.py"
                        # Assume "    :pyobject: xxxxxx"
                        pyobject = line.strip().split(" ")[-1]
                        statement = f"from {module} import {pyobject}"
                        line = statement
                    elif not line.strip():
                        is_literalinclude = False
                        module = ""

                elif is_code and is_rst and line and not line.startswith(" "):
                    # Finish restructured text code block.
                    if not num_code_lines_in_block:
                        self.fail(f"No lines of code in block: {line_index + 1}")
                    is_code = False
                    line = ""
                elif ":emphasize-lines:" in line:
                    line = ""
                elif is_code:
                    # Process line in code block.
                    if is_rst:
                        # Restructured code block normally indented with four spaces.
                        if len(line.strip()):
                            if not line.startswith("    "):
                                self.fail(
                                    "Code line needs 4-char indent: {}: {}".format(
                                        repr(line), doc_path
                                    )
                                )
                            # Strip four chars of indentation.
                            line = line[4:]

                    if len(line.strip()):
                        num_code_lines_in_block += 1
                        num_code_lines += 1
                else:
                    line = ""
                lines.append(line)
                # if orig_line.strip():
                last_line = orig_line

        print("{} lines of code in {}".format(num_code_lines, doc_path))

        # Write the code into a temp file.
        tempfile = NamedTemporaryFile("w+")
        temp_path = tempfile.name
        tempfile.writelines("\n".join(lines) + "\n")
        tempfile.flush()

        # Run the code and catch errors.
        env = os.environ.copy()
        env["PYTHONUNBUFFERED"] = "1"
        proc = Popen([sys.executable, temp_path], close_fds=True, env=env)
        # try:
        #     out, err = proc.communicate(timeout=5)
        # except TimeoutExpired:
        #     proc.terminate()
        #     try:
        #         out, err = proc.communicate(timeout=5)
        #     except TimeoutExpired:
        #         proc.kill()
        #         out, err = proc.communicate(timeout=5)
        # finally:
        #     # Close (deletes) the tempfile.
        #     tempfile.close()

        # # Check for errors running the code.
        # print(out)
        # print(err)
        # out = out.decode("utf8")
        # err = err.decode("utf8")
        # out = out.replace(temp_path, doc_path)
        # err = err.replace(temp_path, doc_path)
        try:
            exit_status = proc.wait(timeout=60)
        except TimeoutExpired:
            proc.terminate()
            try:
                exit_status = proc.wait(timeout=5)
                self.fail(f"Terminated after timeout: {exit_status}")
            except TimeoutExpired:
                proc.kill()
                exit_status = proc.wait()
                self.fail(f"Killed after timeout: {exit_status}")
        else:
            if exit_status:
                self.fail(f"Non-zero exit status: {exit_status}")
        finally:
            # Close (deletes) the tempfile.
            tempfile.close()
