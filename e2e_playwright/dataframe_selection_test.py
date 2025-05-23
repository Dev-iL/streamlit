# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2025)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from playwright.sync_api import Page, expect

from e2e_playwright.conftest import wait_for_app_run

def test_single_cell_selection(app: Page):
    canvas = app.get_by_test_id("stDataFrame").nth(0)
    expect(canvas).to_be_visible()

    # Select a single cell
    cell = canvas.locator("div[data-testid='stDataFrameCell']").nth(0)
    cell.click()
    wait_for_app_run(app)

    # Verify the selection
    expected = "Dataframe single-cell selection: {'selection': {'rows': [0], 'columns': [0]}}"
    selection_text = app.get_by_test_id("stMarkdownContainer").filter(has_text=expected)
    expect(selection_text).to_have_count(1)

def test_multi_cell_selection(app: Page):
    canvas = app.get_by_test_id("stDataFrame").nth(0)
    expect(canvas).to_be_visible()

    # Select multiple cells
    cell1 = canvas.locator("div[data-testid='stDataFrameCell']").nth(0)
    cell2 = canvas.locator("div[data-testid='stDataFrameCell']").nth(1)
    cell1.click()
    app.keyboard.down("Shift")
    cell2.click()
    app.keyboard.up("Shift")
    wait_for_app_run(app)

    # Verify the selection
    expected = "Dataframe multi-cell selection: {'selection': {'rows': [0, 0], 'columns': [0, 1]}}"
    selection_text = app.get_by_test_id("stMarkdownContainer").filter(has_text=expected)
    expect(selection_text).to_have_count(1)
