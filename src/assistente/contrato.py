# from pydantic import BaseModel, model_validator

# class Turma(BaseModel):
#     vagas: int
#     matriculados: int

#     @model_validator(mode= "after")
#     def matriculados_cabem_nas_vagas(self):
#         if self.matriculados > self.vagas:
#             raise ValueError("mais matriculados que vagas")
#         return self

from pydantic import BaseModel, model_validator

class Viagem(BaseModel):
    hora_saida_id: int
    hora_chegada_id: int
    data_saida_id: int
    data_chegada_id: int

    @model_validator(mode="after")
    def viagem_impossivel(self):
        if self.data_saida_id > self.data_chegada_id:
            raise ValueError("impossivel")
        elif self.data_saida_id == self.data_chegada_id and self.hora_saida_id > self.hora_chegada_id:
            raise ValueError("impossivel")
        return self

    # @model_validator(mode="after")
    # def viagem_possivel(self):
    #     if self.data_saida_id < self.data_chegada_id:

