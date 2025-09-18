def _normalize_board(board_str):
    if board_str is None:
        return None

    lines = board_str.strip("\n").splitlines()
    if not lines:
        return None

    valid = set("PBRQNK")
    rows = []
    width = 0
    for line in lines:
        line = line.strip()
        cleaned = ''.join(ch if ch in valid else '.' for ch in line)
        rows.append(cleaned)
        width = max(width, len(cleaned))

    height = len(rows)
    if width != height or width == 0 or width > 8:
        return "invalid"

    rows = [r.ljust(width, '.') for r in rows]
    return rows


def _find_king(rows):
    king_count = 0
    king_pos = None
    for r, line in enumerate(rows):
        for c, ch in enumerate(line):
            if ch == 'K':
                king_count += 1
                king_pos = (r, c)
    
    return king_pos if king_count == 1 else None


def _inside(r, c, h, w):
    return 0 <= r < h and 0 <= c < w


def _ray_hits(rows, kr, kc, attackers, dr, dc):
    h, w = len(rows), len(rows[0])
    r, c = kr + dr, kc + dc
    while _inside(r, c, h, w):
        ch = rows[r][c]
        if ch != '.':              
            return ch in attackers    
        r += dr
        c += dc
    return False


def checkmate(board_str):
    rows = _normalize_board(board_str)
    if rows is None:
        print("invalid board")
        return
    
    if rows == "invalid":
        print("invalid board")
        return

    pos = _find_king(rows)
    if pos is None:
        print("invalid board")
        return

    kr, kc = pos
    h, w = len(rows), len(rows[0])

    #Knight
    knight_moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    for dr, dc in knight_moves:
        r, c = kr + dr, kc + dc
        if _inside(r, c, h, w) and rows[r][c] == 'N':
            print("Success")
            return

    #Pawn
    for dc in (-1, 1):
        r, c = kr + 1, kc + dc
        if _inside(r, c, h, w) and rows[r][c] == 'P':
            print("Success")
            return

    #Bishop / Queen
    for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        if _ray_hits(rows, kr, kc, {'B', 'Q'}, dr, dc):
            print("Success")
            return

    #Rook / Queen
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        if _ray_hits(rows, kr, kc, {'R', 'Q'}, dr, dc):
            print("Success")
            return

    print("Fail")
