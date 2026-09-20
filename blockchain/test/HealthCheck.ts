import { expect } from "chai";
import { ethers } from "hardhat";

describe("Phase 1 Blockchain Toolchain Verification", function () {
  it("Should deploy HealthCheck placeholder contract and return 'pong' from ping()", async function () {
    const HealthCheckFactory = await ethers.getContractFactory("HealthCheck");
    const healthCheck = await HealthCheckFactory.deploy();
    await healthCheck.waitForDeployment();

    const result = await healthCheck.ping();
    expect(result).to.equal("pong");
  });
});
