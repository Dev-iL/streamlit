/**
 * Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import React from "react"

import { screen } from "@testing-library/react"
import "@testing-library/jest-dom"

import { render } from "@streamlit/lib/src/test_util"
import { Block as BlockProto } from "@streamlit/lib/src/proto"

import Popover, { PopoverProps } from "./Popover"

const getProps = (
  elementProps: Partial<BlockProto.Popover> = {},
  props: Partial<PopoverProps> = {}
): PopoverProps => ({
  element: BlockProto.Popover.create({
    label: "label",
    useContainerWidth: false,
    ...elementProps,
  }),
  empty: false,
  ...props,
})

describe("Popover container", () => {
  it("renders without crashing", () => {
    const props = getProps()
    render(
      <Popover {...props}>
        <div>test</div>
      </Popover>
    )
    const popoverButton = screen.getByTestId("stPopover")
    expect(popoverButton).toBeInTheDocument()
  })

  it("renders label as expected", () => {
    const props = getProps()
    render(
      <Popover {...props}>
        <div>test</div>
      </Popover>
    )
    expect(screen.getByText(props.element.label)).toBeInTheDocument()
  })
})
