import unittest
from block_type import *

class TestBlock_to_BlockType(unittest.TestCase):
    def test_Block_to_BlockType_1(self):
        block = "1. line one\n2. line two\n3. line three\n4. line four\n5. line five"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.ORDERED_LIST,
        )
    
    def test_Block_to_BlockType_2(self):
        block = "1. line one\n2. line two\n4. line three\n4. line four\n5. line five"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.ORDERED_LIST,
        )
    
    def test_Block_to_BlockType_3(self):
        block = "### This is a heading Block"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.HEADING,
        )
    
    def test_Block_to_BlockType_4(self):
        block = "- line one\n- line two\n- line three\n- line four\n- line five"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.UNORDERED_LIST,
        )

    def test_Block_to_BlockType_5(self):
        block = ">This is a line in a quote block.\n>This is another line in a quote block.\n>This is a third line in a quote block."
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.QUOTE,
        )

    def test_Block_to_BlockType_6(self):
        block = "```This is a code block.```"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type,
            BlockType.CODE,
        )

    def test_Block_to_BlockType_7(self):
        blocks = [
            "### This is a heading Block",
            "1. line one\n2. line two\n3. line three\n4. line four\n5. line five",
            "```This is a code block.```",
            ">This is a line in a quote block.\n>This is another line in a quote block.\n>This is a third line in a quote block.",
            "This block is just a normal paragraph.\nWith two lines."
        ]
        block_type = []
        for block in blocks:
            block_type.append(block_to_block_type(block))
        self.assertEqual(
            block_type,
            [
                BlockType.HEADING,
                BlockType.ORDERED_LIST,
                BlockType.CODE,
                BlockType.QUOTE,
                BlockType.PARAGRAPH
            ],
        )

if __name__ == "__main__":
    unittest.main()