import re
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_clone(
    name="Veiled",
    ticker="$VEIL",
    ca="0x4663a8B99641D3F82f2c8d2051E840E819F34663",
    twitter="@veiledprivacy",
    email="contact@veiled.space",
    domain="https://veiled.space/",
    launchpad="https://ponsfamily.com/launchpad",
    explorer="https://robinhoodchain.blockscout.com",
    chain_id="4663",
    source_path=os.path.join(SCRIPT_DIR, "source_page.html"),
    output_path=os.path.join(SCRIPT_DIR, "index.html")
):
    with open(source_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    name_lower = name.lower()
    name_cap = name.capitalize()
    
    # 1. Title and basic metadata
    html = re.sub(r'<title>.*?</title>', f'<title>{name_cap} Privacy · Zero-Knowledge State Shield on Robinhood Chain</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="Shield ETH and USDG on Robinhood Chain (EVM {chain_id}) into cryptographic zero-knowledge pools. Fair launching via Pons Family Launchpad with mathematical finality.">', html)
    html = html.replace('content="Hollow"', f'content="{name_cap}"')
    html = html.replace('https://www.usehollow.xyz/hollow-share.png', f'{domain}share.png')
    html = html.replace('https://www.usehollow.xyz/', domain)
    html = html.replace('https://x.com/usehollowxyz', f'https://x.com/{twitter.lstrip("@")}')
    html = html.replace('@usehollowxyz', twitter)
    html = html.replace('contact@usehollow.xyz', email)
    html = re.sub(r'aria-label="Hollow on X[^"]*"', f'aria-label="{name_cap} on X ({twitter})"', html)
    html = html.replace('Hollow home', f'{name_cap} home')
    html = html.replace('Enter Hollow', f'Enter {name_cap}')
    html = html.replace('How Hollow works', f'How {name_cap} works')
    html = html.replace('© 2026 Hollow', f'© 2026 {name_cap} Privacy Protocol · Robinhood Chain')
    html = html.replace('Hollow is an independent project', f'{name_cap} Privacy is an independent decentralized protocol built on Robinhood Chain (Chain ID: {chain_id}). Fair launching via Pons Family Launchpad ({launchpad}). Non-custodial smart contracts.')
    html = html.replace('<span class="sr">Hollow</span>', f'<span class="sr">{name_cap}</span>')
    html = html.replace('<strong>$Hollow</strong>', f'<strong>{ticker}</strong>')

    # 2. Styling Tokens & Accents
    html = html.replace('--accent:#CFE3F5;', '--accent:#A5B4FC;')
    html = html.replace('--hot:#FF8E7A;', '--hot:#FB7185;')
    html = html.replace('--soft:#A9B3BD;', '--soft:#94A3B8;')
    html = html.replace('--ink:#EEF2F6;', '--ink:#F8FAFC;')
    html = html.replace('const ACC = [207, 227, 245];', 'const ACC = [165, 180, 252];')
    html = html.replace("const HOT = '#FF8E7A';", "const HOT = '#FB7185';")

    # 3. Wordmarks & display text
    tracked_word = " ".join(list(name.upper())) if name.upper() == "VEILED" else name_lower
    html = html.replace('<div class="loader-word">hollow</div>', f'<div class="loader-word">{tracked_word}</div>')
    html = html.replace('<span>hollow</span>', f'<span>{tracked_word}</span>')
    html = html.replace('<div class="ghostword" aria-hidden="true">hollow</div>', f'<div class="ghostword" aria-hidden="true">{tracked_word}</div>')
    html = html.replace('<div class="base" aria-hidden="true">hollow</div>', f'<div class="base" aria-hidden="true">{tracked_word}</div>')
    html = html.replace('<div class="lit" aria-hidden="true">hollow</div>', f'<div class="lit" aria-hidden="true">{tracked_word}</div>')

    # 4. Elevated Hero & Story Copy (EVM & Robinhood Chain)
    html = html.replace('Private money · Solana', f'Zero-Knowledge Privacy · Robinhood Chain (EVM {chain_id})')
    html = html.replace('Leave no <em>trace.</em>', 'Silence on the ledger.<br>Leave no <em>shadow.</em>')
    html = html.replace('Shield SOL and USDG, then send and hold with nothing pointing back to you.', f'Shield ETH and USDG into cryptographic zero-knowledge pools on Robinhood Chain. Fair launching via Pons Family Launchpad with zero transaction lineage.')
    html = html.replace('Watch it work <span class="bob">↓</span>', 'Explore Protocol <span class="bob">↓</span>')
    html = html.replace('Live on Solana', f'Robinhood Chain (EVM {chain_id}) · Pons Family Launchpad')

    # Story Phases
    html = html.replace('01 · Exposed', '01 · The Glass Ledger')
    html = html.replace('Your wallet is glass.', 'Your wallet is transparent.')
    html = html.replace('On Solana anyone can watch what you hold and who you pay.', 'On public chains, every transfer, swap, and counterparty is clustered, tracked, and profiled in real time.')
    
    html = html.replace('02 · Shield', '02 · Cryptographic Shield')
    html = html.replace('Step into the hood.', 'Sever on-chain lineage.')
    html = html.replace('One signature drops your SOL or USDG into the shared pool. That is the last thing anyone sees.', 'A single client-side zero-knowledge proof deposits your ETH or USDG on Robinhood Chain into the Merkle accumulator pool. That is the last trace anyone sees.')

    html = html.replace('03 · Blend in', '03 · Anonymity Swarm')
    html = html.replace("Inside, you're noise.", 'Dissolve into noise.')
    html = html.replace("Your coins swirl with everyone else's. Nobody can tell which ones are yours. Not even us.", 'Inside the accumulator, your state blends into thousands of other deposits. Mathematical entropy makes deterministic tracking impossible.')

    html = html.replace('04 · Withdraw', '04 · Clean Withdrawal')
    html = html.replace('Come out anywhere.', 'Emerge untraceable.')
    html = html.replace('Withdraw to a fresh address. Nothing ties it back to where you started.', 'Withdraw clean assets to any unlinked destination wallet. Decentralized relayers sponsor initial gas so your fresh wallet needs zero prior history.')

    # Shell Game (EVM ETH)
    html = html.replace('Watch the coin.', 'The Shuffling Veil.')
    html = html.replace('Try to follow it', 'The Mathematics of Anonymity')
    html = html.replace('Five hoods. One gets your 1 SOL. Keep your eyes on it.', f'Five nodes on Robinhood Chain. One deposit of 0.1 ETH. Watch the shuffle, then track your asset through the zero-knowledge veil.')
    html = html.replace('Drop it in', 'Initiate Shuffle')
    html = html.replace("Which hood has your 1 SOL? Pick one.", "Which node holds your 0.1 ETH? Pick one.")
    html = html.replace("Every hood has 1 SOL. Every exit looks the same, and that's the point.", "Every node holds 0.1 ETH. In the zero-knowledge pool, every exit is identical.")
    html = html.replace('<span class="coin-label">1 SOL</span>', '<span class="coin-label">0.1 ETH</span>')

    # Replace Solana coin path with Ethereum diamond
    old_coin = '''    '<path d="M21.5 18.5 H38.5 L34.5 22.5 H17.5 Z" fill="#3B4B5E"/>' +
    '<path d="M17.5 26 H34.5 L38.5 30 H21.5 Z" fill="#2A3746"/>' +
    '<path d="M21.5 33.5 H38.5 L34.5 37.5 H17.5 Z" fill="#3B4B5E"/>'''

    new_coin = '''    '<polygon points="28,14 38,28 28,33 18,28" fill="#4D6074"/>' +
    '<polygon points="28,14 28,33 18,28" fill="#3B4B5E"/>' +
    '<polygon points="28,35 38,30 28,42" fill="#2A3746"/>' +
    '<polygon points="28,35 28,42 18,30" fill="#3B4B5E"/>'''
    html = html.replace(old_coin, new_coin)

    # Statement & Points
    html = html.replace('<span>Your money.</span><span class="n">Nobody\'s</span><span class="a">business.</span>', '<span>Privacy is not secrecy.</span><span class="n">Privacy is</span><span class="a">sovereignty.</span>')
    html = html.replace('Notes stay with you', 'Client-Side Zero-Knowledge')
    html = html.replace('Proofs are built on your device. Nothing secret ever touches our servers.', 'Proofs are generated locally in WebAssembly inside your browser session. Private keys and secrets never touch external servers.')
    html = html.replace('Your wallet stays hidden', 'Decentralized Relayer Mesh')
    html = html.replace('A relayer submits each withdrawal and pays the fee, so your address never shows up.', 'Independent relayers broadcast withdrawal transactions and pay on-chain fees, completely eliminating origin-to-destination linkages.')
    html = html.replace('Always an exit', 'Guaranteed Non-Custodial Exit')
    html = html.replace('Your deposit can always be withdrawn. Nobody can freeze it, not even us.', 'Smart contracts enforce immutable withdrawal logic. Nobody can freeze, censor, or restrict your deposits. Not even us.')

    # Enter & Footer
    html = html.replace('Step inside', 'Reclaim On-Chain Autonomy')
    html = html.replace('Connect a wallet, unlock your vault, and disappear.', 'Connect your wallet, shield your state, and step into the shadows.')
    html = html.replace('Private money on Solana.', f'Zero-knowledge state shield on Robinhood Chain (EVM {chain_id}).')

    # JavaScript internal events and storage keys
    html = html.replace('hollowLoaded', f'{name_lower}Loaded')
    html = html.replace("'hollow:ready'", f"'{name_lower}:ready'")
    html = html.replace("'hollow:copied'", f"'{name_lower}:copied'")
    html = html.replace("'hollow-seen'", f"'{name_lower}-seen'")

    # Contract address replacement
    if ca:
        html = re.sub(r'data-ca="[a-zA-Z0-9]+"', f'data-ca="{ca}"', html)
        ca_display = ca[:6] + '…' + ca[-4:] if len(ca) > 10 else ca
        html = re.sub(r'<code id="caAddr"[^>]*>.*?</code>', f'<code id="caAddr" data-ca="{ca}" title="{ca}"><span class="ca-full">{ca_display}</span><span class="ca-msg" aria-hidden="true">Copied!</span></code>', html)

    # Relative paths for assets
    html = html.replace('href="/assets/', 'href="./assets/')
    html = html.replace('src="/assets/', 'src="./assets/')
    html = html.replace('href="/favicon.svg"', 'href="./favicon.svg"')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"Generated {output_path} successfully for '{name}' ({ticker}) on Robinhood Chain")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name_arg = sys.argv[1]
        ticker_arg = sys.argv[2] if len(sys.argv) > 2 else f"${name_arg.upper()}"
        generate_clone(name=name_arg, ticker=ticker_arg)
    else:
        generate_clone()
