def settlePokerGame(players, buyInAmount):
    results = []
    totalChips = 0
    totalInvested = 0

    for player in players:
        name = player["name"]
        chips = player["chips"]
        buyIns = player["buyIns"]
        invested = buyIns * buyInAmount
        net = chips - invested

        totalChips += chips
        totalInvested += invested

        results.append({
            "name": name,
            "chips": chips,
            "buyIns": buyIns,
            "invested": invested,
            "net": net
        })

    # 💥 Error check
    if round(totalChips, 2) != round(totalInvested, 2):
        print("  Error: The total chips do not match the total money put into the game.")
        print(f"  Total invested: ${totalInvested:.2f}")
        print(f"  Total chips counted: ${totalChips:.2f}")
        print("  Please check the numbers and try again.")
        return None

    winners = [p for p in results if p["net"] > 0]
    losers = [p for p in results if p["net"] < 0]

    transactions = []

    for loser in losers:
        amountOwed = -loser["net"]
        for winner in winners:
            if winner["net"] == 0:
                continue
            share = min(amountOwed, winner["net"])
            transactions.append(f'{loser["name"]} pays {winner["name"]} ${share:.2f}')
            loser["net"] += share
            winner["net"] -= share
            amountOwed -= share
            if amountOwed <= 0:
                break

    return transactions


def main():
    print("Poker Chip Settlement Calculator")
    numPlayers = int(input("How many players were in the game? "))
    buyInAmount = float(input("What was the buy in amount? $"))

    players = []

    for i in range(numPlayers):
        print(f"\nPlayer {i+1}:")
        name = input("  Name: ")
        buyIns = int(input("  Number of buy-ins: "))
        chips = float(input("  Final chip total: $"))
        players.append({
            "name": name,
            "buyIns": buyIns,
            "chips": chips
        })

    settlements = settlePokerGame(players, buyInAmount)

    if settlements is None:
        return

    print("\n$$$ Settlement Summary:")
    if not settlements:
        print("No one owes anyone anything.")
    else:
        for t in settlements:
            print(t)


if __name__ == "__main__":
    main()