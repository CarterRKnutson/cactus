import os
import sys
from rdkit.Chem import MolFromSmiles, RDConfig

sys.path.append(os.path.join(RDConfig.RDContribDir, "SA_Score"))
import sascorer
from langchain.tools import BaseTool


class calculate_SA(BaseTool):
    name = "calculate_TPSA"
    description = "Compute the topological surface area (TPSA) of the given molecule."

    def _run(self, compound: str) -> float:
        """
        Compute Synthetic Accessibility (SA) of the given molecule. Ertl & Schuffenhauer 2009.

        Parameters:
        compound: Compound in SMILES format

        Returns:
        float: The SA between 1 (easy) and 10 (hard)
        """
        return sascorer.calculateScore(MolFromSmiles(compound))

    async def _arun(self, compound: str) -> float:
        """Use the convert_to_SMILES tool asynchronously."""
        raise NotImplementedError()
