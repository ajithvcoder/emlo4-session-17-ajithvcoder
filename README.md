
eksctl create cluster -f eks-cluster.yaml
eksctl delete cluster -f eks-cluster.yaml --disable-nodegroup-eviction
### KNative
https://medium.com/@cloudspinx/fix-error-metrics-api-not-available-in-kubernetes-aa10766e1c2f

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.16.0/serving-crds.yaml
kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.16.0/serving-core.yaml

kubectl apply -f https://github.com/knative/net-istio/releases/download/knative-v1.16.0/istio.yaml
###-------- kubectl apply -l knative.dev/crd-install=true -f https://github.com/knative/net-istio/releases/download/knative-v1.16.0/istio.yaml
kubectl apply -f https://github.com/knative/net-istio/releases/download/knative-v1.16.0/istio.yaml
kubectl apply -f https://github.com/knative/net-istio/releases/download/knative-v1.16.0/net-istio.yaml

kubectl patch configmap/config-domain \
      --namespace knative-serving \
      --type merge \
      --patch '{"data":{"emlo.tsai":""}}'

kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.16.0/serving-hpa.yaml
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.16.2/cert-manager.yaml

kubectl get all -n cert-manager

# Wait for cert manager pods to be ready

kubectl apply --server-side -f https://github.com/kserve/kserve/releases/download/v0.14.1/kserve.yaml

### Wait for KServe Controller Manager to be ready

kubectl apply --server-side -f https://github.com/kserve/kserve/releases/download/v0.14.1/kserve.yaml

kubectl get all -n kserve

kubectl apply --server-side -f https://github.com/kserve/kserve/releases/download/v0.14.1/kserve-cluster-resources.yaml

### Create S3 Service Account
### Create IRSA for S3 Read Only Access

eksctl create iamserviceaccount \
--cluster=basic-cluster \
--name=s3-read-only \
--attach-policy-arn=arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess \
--override-existing-serviceaccounts \
--region ap-south-1 \
--approve

kubectl apply -f s3-secret.yaml
kubectl patch serviceaccount s3-read-only -p '{"secrets": [{"name": "s3-secret"}]}'

do torchserve works


kubectl apply -f vit-classifier.yaml

kubectl
kubectl get isvc


kubectl get isvc

kubectl get svc -n istio-system

prometheus and grafana

git clone --branch release-0.14 https://github.com/kserve/kserve.git
cd kserve
kubectl apply -k docs/samples/metrics-and-monitoring/prometheus-operator
kubectl wait --for condition=established --timeout=120s crd/prometheuses.monitoring.coreos.com
kubectl wait --for condition=established --timeout=120s crd/servicemonitors.monitoring.coreos.com
kubectl apply -k docs/samples/metrics-and-monitoring/prometheus

Test if Prometheus is working

kubectl port-forward service/prometheus-operated -n kfserving-monitoring 9090:9090

kubectl patch configmaps -n knative-serving config-deployment --patch-file qpext_image_patch.yaml

kubectl delete -f vit-classifier.yaml
kubectl apply -f vit-classifier.yaml

eksctl scale nodegroup --cluster=basic-cluster --nodes=6 ng-spot-3 --nodes-max=6
eksctl get nodegroup --cluster basic-cluster --region ap-south-1 --name ng-spot-3
Grafana
kubectl create namespace grafana

helm search hub grafana

helm repo add grafana https://grafana.github.io/helm-charts

helm repo update

helm install grafana grafana/grafana --namespace grafana --version 8.8.4

#### -- kubectl get secret --namespace grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
kubectl get secret --namespace grafana grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
kubectl port-forward svc/grafana 3000:80 -n grafana

kubectl get isvc

Just apply the new canary

<debug>
kubectl port-forward service/prometheus-operated -n kfserving-monitoring 9090:9090
http://prometheus-operated.kfserving-monitoring.svc.cluster.local:9090

Not able to connect prometheus and grafana
------------

kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

ArgoCD

curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
rm argocd-linux-amd64

argocd admin initial-password -n argocd

kubectl port-forward svc/argocd-server -n argocd 8080:443 --address 0.0.0.0
argocd login --port-forward --port-forward-namespace argocd --plaintext 127.0.0.1:9000

argocd not rechable
kubectl port-forward svc/argocd-server -n argocd 8080:443
kubectl port-forward svc/argocd-server -n argocd --address 0.0.0.0  8080:443
kubectl port-forward svc/doc-deployment --address 0.0.0.0 5000:80

work till 10.00 pm and get everything fixed today.(power week)

kubectl apply -f argo-apps

<debug>
ajith@LAPTOP-OVJI4T62:~/mlops/course/emlo_play/emlo4-s17/emlo4-session-17-ajithvcoder-canary-argocd-kserve$ kubectl apply -f argo-apps
application.argoproj.io/model-deployments created
secret/s3creds created
Warning: resource serviceaccounts/s3-read-only is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
serviceaccount/s3-read-only configured
</debug>

or", use_fast=True)
2025-02-06T17:58:51,964 [INFO ] W-9000-imagenet-vit_1.0-stdout MODEL_LOG -   File "/home/venv/lib/python3.9/site-packages/transformers/models/auto/image_processing_auto.py", line 403, in from_pretrained
2025-02-06T17:58:51,964 [INFO ] W-9000-imagenet-vit_1.0-stdout MODEL_LOG -     raise ValueError(
2025-02-06T17:58:51,966 [INFO ] W-9000-imagenet-vit_1.0-stdout MODEL_LOG - ValueError: Unrecognized image processor in /home/model-server/tmp/models/31a8c3f52d7d49a3bf7df9c287e9f878/processor. Should have a `image_processor_type` key in its preprocessor_config.json of config.json, or one of the following `model_type` keys in its config.json: align, beit, bit, blip, blip-2, bridgetower, chinese_clip, clip, clipseg, conditional_detr, convnext, convnextv2, cvt, data2vec-vision, deformable_detr, deit, deta, detr, dinat, dinov2, donut-swin, dpt, efficientformer, efficientnet, flava, focalnet, git, glpn, groupvit, idefics, imagegpt, instructblip, layoutlmv2, layoutlmv3, levit, mask2former, maskformer, mgp-str, mobilenet_v1, mobilenet_v2, mobilevit, mobilevitv2, nat, nougat, oneformer, owlvit, perceiver, pix2struct, poolformer, pvt, regnet, resnet, sam, segformer, swiftformer, swin, swin2sr, swinv2, table-transformer, timesformer, tvlt, upernet, van, videomae, vilt, vit, vit_hybrid, vit_mae, vit_msn, vitmatte, xclip, yolos
https://discuss.huggingface.co/t/error-finding-processors-image-class-loading-based-on-pattern-matching-with-feature-extractor/31890/11


debugging
eksctl scale nodegroup --cluster=basic-cluster --nodes=6 ng-spot-3 --nodes-max=6

problem might be with 
      modelFormat:
        name: pytorch
pytorch image in yaml file of argocd, so use different images for different model-deployments and see.
first test food-classifier alone seperately and see.