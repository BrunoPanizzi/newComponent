# newComponent
A small python scirpt to create React components with styled-components

## Usage

To use the program, make sure that you have python3 installed and then clone the repo.
After that, just go to the root of any React project and run the script followed by the name of the component that you want to create

The script creates a folder with the name of the component inside the `components` directory, if there is no such directory, the script throws an error.
The new component folder structure is as follows:

```
┌─────────────────────┐
│ components          │
│  │                  │
│  ├──► index.ts      │  // just exports the component
│  │                  │
│  ├──► Component.tsx │  // the component itself 
│  │                  │
│  └──► styles.ts     │  // imports styled and exports Container
└─────────────────────┘
```

### Future goals
- add flag to use `js` instead of `ts`
- add flag to create or not the `index` file
- maybe create a VsCode/NeoVim extension??
