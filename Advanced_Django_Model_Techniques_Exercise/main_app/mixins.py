from django.db import models


class RechargeEnergyMixin:
    def recharge_energy(self, amount: int):
        self.energy = self.energy + amount if self.energy + amount < 100 else 100
        # self.energy = min(100, self.energy + amount) - > coolway
        self.save()