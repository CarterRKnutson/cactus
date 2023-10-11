from rdkit.Chem import MolFromSmiles, Descriptors
from langchain.tools import BaseTool


class calculate_MolWt(BaseTool):
    name = "calculate_MolWt"
    description = """
    Compute the exact molecular weight of the given molecule. Input should be a SMILES string,
    convert if necessary.
    """

    def _run(self, compound: str) -> float:
        """
        Compute the exact molecular weight of the given molecule.

        Parameters:
        compound: Compound in SMILES format

        Returns:
        float: The exact molecular weight in daltons
        """
        mol = MolFromSmiles(compound)
        return Descriptors.ExactMolWt(mol)

    async def _arun(self, compound: str) -> float:
        """Use the convert_to_SMILES tool asynchronously."""
        raise NotImplementedError()
