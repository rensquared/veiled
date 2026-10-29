# V E I L E D

> **Silence on the ledger. Leave no shadow.**

An EVM-native, zero-knowledge state shield engineered for **Robinhood Chain (EVM 4663)**.

Official Website: [https://veiled.space/](https://veiled.space/)  
Official X / Twitter: [@veiledprivacy](https://x.com/veiledprivacy)  
Block Explorer: [robinhoodchain.blockscout.com](https://robinhoodchain.blockscout.com)  

---

## Overview

Public blockchains cluster, track, and profile wallet activities in real time. **VEILED** introduces client-side zero-knowledge state shielding to Robinhood Chain, enabling users to shield native `ETH` and `USDC` into Poseidon Merkle accumulators, break transaction graph lineage, and withdraw clean funds to unlinked destination addresses via decentralized relayers.

### Core Architecture

1. **Client-Side Zero-Knowledge Prover**: Generates Groth16 zk-SNARK proofs entirely in-browser via WebAssembly. Private keys and nullifier secrets never touch external infrastructure.
2. **Poseidon Merkle Accumulator**: On-chain cryptographic state tree maintaining commitment sets with mathematical finality.
3. **Decentralized Relayer Mesh**: Independent relayers sponsor destination gas and broadcast withdrawal transactions, guaranteeing total severance of on-chain lineage ($✕\text{ NO LINK}$).
4. **The Shuffling Veil ($5\text{ in }5$ Anonymity Set)**: An interactive 5-node cryptographic mixing model featuring the Council of Five Veiled Sentinels demonstrating that every exit from the pool is mathematically indistinguishable.

---

## Network Configurations

### Robinhood Chain (Mainnet)
* **Chain ID**: `4663`
* **Currency Symbol**: `ETH`
* **Default RPC URL**: `https://rpc.mainnet.chain.robinhood.com/`
* **Block Explorer**: [robinhoodchain.blockscout.com](https://robinhoodchain.blockscout.com)

### Robinhood Chain Testnet
* **Chain ID**: `46630`
* **Currency Symbol**: `ETH`
* **Default RPC URL**: `https://rpc.testnet.chain.robinhood.com/`
* **Block Explorer**: [explorer.testnet.chain.robinhood.com](https://explorer.testnet.chain.robinhood.com)

---

## Local Development

The web client is completely self-contained with zero external CDN dependencies:

```bash
# Clone the repository
git clone https://github.com/rensquared/veiled.git
cd veiled

# Run local development server
python -m http.server 3000
```

Open `http://localhost:3000/` in your browser.

---

## Documentation

* [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md): Master technical specifications and project background.
* [WALKTHROUGH.md](WALKTHROUGH.md): Cryptographic protocol deep dive, sequence diagrams, and mathematical breakdown.
* [TWITTER_FLOW.md](TWITTER_FLOW.md): Launch narrative, thread structures, and community communications.

---

## License

MIT © 2026 VEILED Protocol. Built on Robinhood Chain.
