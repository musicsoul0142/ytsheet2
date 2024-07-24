#################### 基本設定 ####################
use strict;
use utf8;

package set;

## ●管理ユーザーID
 # 指定したIDは全シートの閲覧と編集ができます。
 # our $masterid = '337954988204621835';

## ●登録関係
 # 登録キー
  our $registerkey = '';
 # データ作成・編集にユーザー登録（ログイン状態）を必須にする
  our $user_reqd = 1;
 # キャラクター・魔物のIDをランダムではなくユーザーID＋番号(001,002..)にする(魔物はm001..)
  our $id_type = 0;

## ●OAuth2 でのログイン関係
 # OAuth2 を提供するサービスの名称。現在 Discord と Google のみ対応
  our $oauth_service = 'Discord';
 # OAuth2 で利用するサービスにユーザがログインするための URL
  our $oauth_login_url = 'https://discord.com/oauth2/authorize?client_id=1264787503450427422&response_type=code&redirect_uri=https%3A%2F%2Fginrin.f5.si%2Fytsheet2%2Far2e%2Foauth.cgi&scope=identify+guilds+email';
 # OAuth2 で利用するサービスから払い出される client_id
  our $oauth_client_id = '1264787503450427422';
 # OAuth2 で利用するサービスから払い出される client_secret
  our $oauth_secret_id = 'nnktYZlV4fK_pcBKGTM2sXXdEmbF3dH1';
 # ゆとシート2 の URL のうち index.cgi を oauth.cgi に置換したもの
  our $oauth_redirect_url = 'https://ginrin.f5.si/ytsheet2/ar2e/oauth.cgi';
 # OAuth2 のスコープ
  our $oauth_scope = 'identify+guilds+email';

 # OAuth で Discord を利用する場合のみ利用可能 ログインを許可する Discord のサーバ一覧。空リストの場合は制限しない
  our @oauth_discord_login_servers = ('895463252354551868'); 
  
## ●タイトル
 # ページ左上のタイトル
  our $title = 'ゆとシートⅡ for AR2E - 銀輪鯖';
  
## ●画像関係
 # キャラクター画像のファイルサイズ上限(単位byte)
  our $image_maxsize = 1024 * 1024 * 1;
 # 画像警告
  our $image_notice = '著作権上の問題がないか確認したうえで投稿してください。また、R-18にあたるような画像はおやめください。';
## ●削除関係
 # データを削除するとき、バックアップも削除 する=1 しない=0
  our $del_back = 0;
  
## ●グループ設定
 # ["ID", "ソート順(空欄で非表示)", "分類名", "分類の説明文"],
 # 選択時はここで書いた順番、キャラ一覧(グループ別)ではソート順で数字が小さい方から表示されます
 # 増減OK
  our @groups = (
    ["pc",  "01", "PC", "プレイヤーキャラクター"],
    ["npc", "99", "NPC", "ノンプレイヤーキャラクター"],

   # ["A", "01", "キャンペーン「A」", "GM：○○"],
   # ["B", "02", "キャンペーン「B」", "GM：××"],
   # ["", "", "", ""],
  );
  
 # デフォルトのグループID
  our $group_default = 'pc';

 # トップページのキャラクター最大表示数（1グループあたり／無制限=0）
  our $list_maxline = 0; 

 # グループ個別表示時や検索結果表示時の1ページあたりの最大表示数（0で全部表示）
  our $pagemax = 0;

## ●キャラクターシートの各種初期値
  our $make_exp   = 15;  # 初期成長点
  our $make_money = 1200;  # 初期所持金
  our $make_fix   = 0;  # 初期値を固定にする(PLが変更出来ないようにする)=1 しない=0

## ●ログイン関係ファイル
 # ユーザー情報・ログイン状態はデフォルトでは別システム（別ディレクトリ）でも共通です。
 # ユーザー情報・ログイン状態を別にしたい場合、以下の設定にしてください（コメントアウト#を解除ください）。
 # our $userfile    = './data/users.cgi';       # ユーザー一覧ファイル
 # our $login_users = './data/login_users.cgi'; # ログイン情報保存ファイル
 # our $tokenfile   = './data/token.cgi';       # 一時トークン保存ファイル

  our $admimail = 'noreply@ginrin.f5.si'; # 管理者メールアドレス

## 上記以外の設定は lib/config-default.pl を参照してください。 ##

1;