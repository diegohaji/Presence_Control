# Controle de Presenca em Ambiente

## What This Is

Um sistema de visao computacional para detectar pessoas em video, rastrear seus deslocamentos e contar entradas e saidas quando elas cruzam uma linha virtual. O projeto deve funcionar tanto com webcam quanto com arquivo de video, sem assumir um unico tipo de ambiente: porta, corredor, catraca ou sala ampla podem ser usados como cenarios de validacao.

O entregavel inicial e um contador em tempo real com sobreposicao visual e log de eventos de entrada/saida. A prioridade e contagem correta; desempenho em tempo real vem logo em seguida.

## Core Value

Contar corretamente entradas e saidas de pessoas ao cruzarem uma linha virtual em video, registrando cada evento de forma auditavel.

## Requirements

### Validated

(None yet - ship to validate)

### Active

- [ ] Capturar video de webcam e de arquivos locais.
- [ ] Permitir configuracao de uma linha virtual no frame.
- [ ] Detectar pessoas no video usando modelo de segmentacao/deteccao compativel com COCO.
- [ ] Rastrear pessoas entre frames com IDs temporarios.
- [ ] Contar entrada e saida quando uma pessoa cruza a linha na direcao correspondente.
- [ ] Exibir contadores e marcacoes no video em tempo real.
- [ ] Registrar eventos de entrada/saida em log persistente.
- [ ] Permitir validacao em videos proprios gravados por webcam ou celular.

### Out of Scope

- Identificacao individual, reconhecimento facial ou biometria - o projeto conta fluxos, nao identifica pessoas.
- Controle de acesso fisico ou integracao com catracas - o foco e visao computacional e log.
- Multi-camera sincronizado - aumenta muito a complexidade e nao e necessario para o v1.
- Dashboard web/cloud - o primeiro valor esta no contador local e auditavel.
- Treinamento completo de modelo do zero - o v1 deve usar pesos pretreinados ou fine-tuning leve quando necessario.
- Garantia de precisao em ambientes lotados com oclusao severa - isso exige avaliacao e modelos mais robustos em versoes futuras.

## Context

A ideia original define um contador de presenca em ambiente com linha virtual, contador automatico, OpenCV, segmentation_models_pytorch, tracking simples por centroid ou ByteTrack, COCO Dataset e videos proprios de webcam/celular.

O sistema deve ser tratavel como uma aplicacao local de laboratorio/prototipo: uma pessoa roda o programa, escolhe a fonte de video, ajusta a linha virtual, observa a contagem e recebe um log de eventos. Como nao ha um ambiente especifico fixado, a arquitetura precisa ser parametrizavel o suficiente para adaptar a linha, direcao e limiares sem mudar codigo.

O usuario confirmou que o cenario pode ser porta, sala, corredor ou catraca; a fonte deve aceitar webcam e arquivo; e a prioridade e contagem correta, seguida por tempo real.

## Constraints

- **Tech stack**: Python, OpenCV, PyTorch e segmentation_models_pytorch - estas tecnologias foram indicadas na ideia inicial.
- **Video input**: Webcam e arquivo local - ambos foram confirmados para o primeiro entregavel.
- **Counting model**: Linha virtual com direcao - e o mecanismo central do produto.
- **Tracking**: Comecar simples com centroid tracking e manter interface para ByteTrack - reduz risco inicial e preserva caminho de melhoria.
- **Dataset**: COCO e videos proprios - COCO ajuda com classe pessoa; videos proprios validam o ambiente real.
- **Priority**: Correcao da contagem antes de FPS - evita otimizar uma contagem errada.
- **Privacy**: Nao armazenar identidade pessoal - logs devem registrar eventos de contagem, nao identidade.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| V1 aceita webcam e arquivo de video | Permite teste em tempo real e reproducao de cenarios gravados | Pending |
| Projeto nao fixa um unico cenario fisico | O usuario quer flexibilidade entre porta, sala, corredor ou catraca | Pending |
| Contagem correta tem prioridade sobre FPS | Dupla contagem e direcao errada invalidam o entregavel | Pending |
| Centroid tracking e o caminho inicial, ByteTrack fica plugavel | Reduz complexidade inicial sem fechar a porta para tracking mais robusto | Pending |
| Logs registram eventos de entrada/saida, nao identidade | Mantem foco em presenca e reduz risco de privacidade | Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `$gsd-transition`):
1. Requirements invalidated? -> Move to Out of Scope with reason
2. Requirements validated? -> Move to Validated with phase reference
3. New requirements emerged? -> Add to Active
4. Decisions to log? -> Add to Key Decisions
5. "What This Is" still accurate? -> Update if drifted

**After each milestone** (via `$gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check - still the right priority?
3. Audit Out of Scope - reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-05-18 after initialization*
