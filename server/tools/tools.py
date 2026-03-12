"""
This module contains tools for managing Trello boards, lists, and cards.
Set LITE=true in .env for a minimal read-only tool surface (local model friendly).
"""

import os

from server.tools import card, checklist


def register_tools(mcp):
    """Register tools with the MCP server."""
    if os.getenv("LITE", "false").lower() == "true":
        mcp.add_tool(card.get_cards)
        mcp.add_tool(card.get_card)
        mcp.add_tool(card.get_card_comments)
        mcp.add_tool(checklist.get_card_checklists_summary)
        return

    from server.tools import board, list

    mcp.add_tool(board.get_board)
    mcp.add_tool(board.get_boards)
    mcp.add_tool(board.get_board_labels)
    mcp.add_tool(board.create_board_label)

    mcp.add_tool(list.get_list)
    mcp.add_tool(list.get_lists)
    mcp.add_tool(list.create_list)
    mcp.add_tool(list.update_list)
    mcp.add_tool(list.delete_list)

    mcp.add_tool(card.get_card)
    mcp.add_tool(card.get_cards)
    mcp.add_tool(card.create_card)
    mcp.add_tool(card.update_card)
    mcp.add_tool(card.delete_card)

    mcp.add_tool(checklist.get_checklist)
    mcp.add_tool(checklist.get_card_checklists)
    mcp.add_tool(checklist.create_checklist)
    mcp.add_tool(checklist.update_checklist)
    mcp.add_tool(checklist.delete_checklist)
    mcp.add_tool(checklist.add_checkitem)
    mcp.add_tool(checklist.update_checkitem)
    mcp.add_tool(checklist.delete_checkitem)
