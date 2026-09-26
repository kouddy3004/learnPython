from learnDataEngineer.stockAnalysis.stockFromGit.stockFromGitRepo import getStocksFromRepoAndExtractSectorResult
from learnDataEngineer.stockAnalysis.stockFromGit.constants import Constants

inAws = False
const = Constants(inAws)

result = getStocksFromRepoAndExtractSectorResult(const, inAWS=inAws)
print(result)
